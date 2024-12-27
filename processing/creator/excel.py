import subprocess
from pathlib import Path

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.workbook.workbook import Workbook

from processing.enumerations import TaillePapier as T
from processing.decrypt import APPLESCRIPT



class Excel:
    def convertXlsxToPDF(self, Fichier, pageName=None):
        """
        Converti un Fichier Excel en PDF avec windows et mac
        :param Fichier: Chemin vers le fichier source
        :param pageName: Nom de la feuille pour l'APPLESCRIPT
        :return: Chemin vers le fichier PDF
        """
        pdfPath = None
        if self.systeme == "Windows":
            from win32com.client import Dispatch

            xlsx = Path(Fichier).as_posix()
            pdfPath = Path(xlsx).with_suffix(".pdf")
            excel = Dispatch("Excel.Application")
            excel.Visible = False
            try:
                wb = excel.Workbooks.Open(xlsx)
                wbk = openpyxl.load_workbook(xlsx)
                wb.WorkSheets(wbk.sheetnames).Select()
                wb.ActiveSheet.ExportAsFixedFormat(0, pdfPath)
            except Exception as e:
                self.updateLog(
                    "Le programme n'a pas pu convertir en PDF",
                    titre="non",
                    color="#E74C3C",
                )
                pdfPath = None
            else:
                pass
            finally:
                wb.Close()
                excel.Quit()
                wbk.close()
        elif self.systeme == "Darwin":
            try:
                script_path = Path().home() / "Documents" / "exceltopdf.scpt"
                xlsx = Path(Fichier).as_posix()
                pdfPath = Path(xlsx).with_suffix(".pdf")
                APPLESCRIPT_content = (
                    APPLESCRIPT.replace("<@ExcelPath>", xlsx)
                    .replace("<@PDFPath>", pdfPath.as_posix())
                    .replace("<@SheetName>", pageName)
                )
                with script_path.open("w") as script_file:
                    script_file.write(APPLESCRIPT_content.strip())

                subprocess.run(["osascript", str(script_path)], check=True)
            except subprocess.CalledProcessError as e:
                self.forceSuppression(script_path)
                pdfPath = None
        return pdfPath

    def mise_en_page(self, **kwargs):
        """
        Création d'une mise en page pour une impression.
        :key wb (Workbook): Instance du classeur à utiliser.
        :key ws (Worksheet): Feuille de calcul active pour la mise en page.
        :key sauvegarde (Path): Le chemin de sauvegarde.
        :key area (str): Plage de cellules à mettre en page (ex: 'A1:D10').
        :key orientation (str): Orientation de la page ('portrait' ou 'paysage').
        :key margin (dict): Marges de la page en pouces.
        :key grillage (bool): Indique si la grille doit être affichée.
        :key apercu (str): Mode d'aperçu avant impression.
        :key zoom (int): Niveau de zoom pour l'affichage.
        :key largPage (float): Nombre de pages en largeur.
        :key hautPage (float): Nombre de pages en hauteur.
        :key PAPERSIZE (TaillePapier): Taille du papier (ex: 'A4', 'Letter').
        :key cheight (float): Hauteur personnalisée de la page.
        :key cwidth (float): Largeur personnalisée de la page.
        :key HeadCenter (str): Texte de l'en-tête centré.
        :key HeadRight (str): Texte de l'en-tête aligné à droite.

        """
        # configuration des parametres
        wb = kwargs["wb"]
        ws = kwargs["ws"]
        sauvegarde = kwargs["sauvegarde"]
        margin = kwargs.get("margin", self.JSON.MARGINF)
        largPage = kwargs.get("largPage", 1)
        hautPage = kwargs.get("hautPage", 1)
        # configuration des tailles papier
        taille = {t: getattr(ws, t.value) if t.name != "CUSTOM" else t.value for t in T}

        ws.page_setup.paperSize = taille.get(kwargs.get("PAPERSIZE", T.A4))
        ws.page_setup.orientation = (
            ws.ORIENTATION_PORTRAIT
            if kwargs.get("orientation", "portrait") == "portrait"
            else ws.ORIENTATION_LANDSCAPE
        )
        ws.print_area = kwargs.get("area", "A1:B1")
        ws.page_margins = openpyxl.worksheet.page.PageMargins(**margin)
        ws.sheet_view.showGridLines = kwargs.get("grillage", True)
        if kwargs.get("PAPERSIZE", T.A4) == T.CUSTOM:
            ws.page_setup.paperHeight = f"{kwargs.get('cheight', 420)}mm"
            ws.page_setup.paperWidth = f"{kwargs.get('cwidth', 297)}mm"
        ws.page_setup.fitToWidth = False if not isinstance(largPage, int) else largPage
        ws.page_setup.fitToHeight = False if not isinstance(hautPage, int) else hautPage
        ws.page_setup.horizontalCentered = True
        ws.page_setup.verticalCentered = True
        # Configuration du centrage lors de l'impression
        ws.print_options.horizontalCentered = True  # Centrage horizontal
        # ws.print_options.verticalCentered = True    # Centrage vertical
        ws.sheet_properties.pageSetUpPr.fitToPage = True

        ws.sheet_view.view = kwargs.get(
            "apercu", "normal"
        )  # 'normal, "pageBreakPreview" , 'pageLayout'
        ws.sheet_view.zoomToFit = True
        # Recherche la colonne maximum
        _, _, MC, _ = openpyxl.utils.range_boundaries(kwargs.get("area", "A1:B1"))
        ws.column_dimensions[openpyxl.utils.get_column_letter(MC)].width = 3
        if kwargs.get("zoom"):
            ws.sheet_view.zoomScale = kwargs.get("zoom")
        wb.save(sauvegarde)

    def pied_page(self, **kwargs):
        """
        insertion d'un pied de page Excel
        :param wb: Workbook
        :param ws: Worksheet
        :param sauvegarde: sauvegarde du fichier
        :param gauche: gauche de page
        :param droite: droite de page
        :param centre: centre de page
        :return:
        """
        wb: Workbook = kwargs["wb"]
        ws: Worksheet = kwargs["ws"]
        gauche = kwargs.get("gauche", "&P sur &N")
        centre = kwargs.get("centre", self.TEXT.FOOTER_FACTURE)
        droite = kwargs.get("droite")
        ws.oddFooter.center.text = centre
        ws.oddFooter.left.text = gauche
        ws.oddFooter.right.text = droite
        ws.oddHeader.size = 16
        ws.oddHeader.font = "Arial,Bold"
        wb.save(kwargs.get("sauvegarde"))

    def CentrerMultipleCols(self, workbook: Workbook, worksheet: Worksheet, cell_range: str, sauvegarde: Path):
        """
        Center sur plusieur colonnes du worksheet

        :param workbook: Classeur
        :param worksheet: Feuille
        :param cell_range: Plage des cellules à centrer le texte
        :param sauvegarde: chemin du fichier de sauvegarde
        :return: None
        """
        for row in worksheet[cell_range]:
            for cell in row:
                alignment = cell.alignment.copy()
                alignment.horizontal = "centerContinuous"
                cell.alignment = alignment
        workbook.save(sauvegarde)

    def BordureExterieur(self, workbook, worksheet, bordure, limin: int, limax: int, colmin: int, colmax: int, sauvegarde: str,):
        """
        Donne une bordure exérieur sans effacer le style
        :param workbook: Claseur
        :param worksheet: Feuille
        :param bordure: Type de bordure
        :param limin: numero de ligne minimum
        :param limax: numero de ligne maximum
        :param colmin: numero de colonnes minimum
        :param colmax: numero de colonnes maximum
        :param sauvegarde: Fichier de sauvegarde
        :Example:
        >>> pour centrer de A1 à C1 : self.BordureExterieur(wb, ws, thin, 1, 1, 1, 3, "fichier.xlsx")
        :return: None
        """
        for row in worksheet.iter_rows(
            min_row=limin, max_row=limax, min_col=colmin, max_col=colmax
        ):
            for cell in row:
                lettre, ligne = openpyxl.utils.cell.coordinate_from_string(
                    cell.coordinate
                )
                index_colonne = openpyxl.utils.column_index_from_string(lettre)
                b = {
                    "left": bordure if (index_colonne == colmin) else cell.border.left,
                    "top": (
                        bordure
                        if (ligne == limin or limin == limax)
                        else cell.border.top
                    ),
                    "right": (
                        bordure if (index_colonne == colmax) else cell.border.right
                    ),
                    "bottom": (
                        bordure
                        if (ligne == limax or limin == limax)
                        else cell.border.bottom
                    ),
                }
                cell.border = openpyxl.styles.Border(**b)
        workbook.save(sauvegarde)

    def ajouter_validation_liste(self, **kwargs):
        """
        Ajoute une validation de liste à une plage de cellules.

        :key worksheet: La feuille de calcul
        :key colonne: La lettre de la colonne (ex: 'B')
        :key debut_ligne: Première ligne de la validation
        :key fin_ligne: Dernière ligne de la validation
        :key options: Liste des options pour la validation directe
        :key plage_reference: Plage de cellules de référence (ex: '=$A$1:$A$5')
        """
        worksheet = kwargs.get('ws')
        colonne = kwargs.get('col')
        debut_ligne = kwargs.get('debut_ligne')
        fin_ligne = kwargs.get('fin_ligne')
        options = kwargs.get('options')
        plage_reference = kwargs.get('plage_reference')

        # Convertir la colonne en lettre si elle est numérique
        if isinstance(colonne, int):
            colonne = openpyxl.utils.cell.get_column_letter(colonne)

        if options and plage_reference:
            raise ValueError("Spécifiez soit options soit plage_reference, pas les deux")

        if not options and not plage_reference:
            raise ValueError("Spécifiez au moins options ou plage_reference")

        validation = DataValidation(
            type="list",
            formula1=f'"{",".join(options)}"' if options else plage_reference,
            allow_blank=True,
            error="Veuillez choisir une option valide",
            errorTitle="Erreur de saisie",
            prompt="Sélectionnez une option dans la liste",
            promptTitle="Liste de choix"
        )

        worksheet.add_data_validation(validation)
        validation.add(f'{colonne}{debut_ligne}:{colonne}{fin_ligne}')