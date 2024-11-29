from PySide6.QtCore import (
    QPropertyAnimation,
    QEasingCurve,
    QPoint,
    QTimer,
)
from processing.enumerations import LevelCritic


class AnimationForm:

    def schedule_hide_notification(self, text):
        word_count = len(text.split())
        display_duration = int((word_count / 4) * 1000)
        QTimer.singleShot(display_duration, self.hide_notification)

    def show_notification(self, message: str, level: LevelCritic):

        self.notification.setText(message)
        self.notification.setLevel(level)

        if (
            self.animationShowNotification
            and self.animationShowNotification.state() == QPropertyAnimation.Running
        ):
            return
        if (
            self.animationHideNotification
            and self.animationHideNotification.state() == QPropertyAnimation.Running
        ):
            self.animationHideNotification.stop()

        start_pos = QPoint(
            self.width(), self.height() - (self.notification.height() + 50)
        )
        end_pos = QPoint(
            self.width() - (self.notification.width() + 10),
            self.height() - (self.notification.height() + 20),
        )

        self.notification.move(start_pos)
        self.notification.show()

        self.animationShowNotification = QPropertyAnimation(self.notification, b"pos")
        self.animationShowNotification.setDuration(1000)
        self.animationShowNotification.setStartValue(start_pos)
        self.animationShowNotification.setEndValue(end_pos)
        self.animationShowNotification.setEasingCurve(QEasingCurve.InOutCubic)
        self.animationShowNotification.finished.connect(
            lambda: self.schedule_hide_notification(message)
        )
        self.animationShowNotification.start()

    def hide_notification(self):
        if (
            self.animationHideNotification
            and self.animationHideNotification.state() == QPropertyAnimation.Running
        ):
            return

        start_pos = self.notification.pos()
        end_pos = QPoint(self.width(), self.notification.pos().y())

        self.animationHideNotification = QPropertyAnimation(self.notification, b"pos")
        self.animationHideNotification.setDuration(1000)
        self.animationHideNotification.setStartValue(start_pos)
        self.animationHideNotification.setEndValue(end_pos)
        self.animationHideNotification.setEasingCurve(QEasingCurve.InOutCubic)
        self.animationHideNotification.finished.connect(self.notification.hide)
        self.animationHideNotification.start()