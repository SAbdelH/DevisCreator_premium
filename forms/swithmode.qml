import React, { useState } from 'react';
import { Switch } from '@/components/ui/switch';
import { Sun, Moon } from 'lucide-react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const DarkLightModeSwitch = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };

  return (
    <Card className={`w-full max-w-md ${isDarkMode ? 'bg-gray-800 text-white' : ''}`}>
      <CardHeader>
        <CardTitle>Dark/Light Mode</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex items-center justify-between">
          {isDarkMode ? (
            <Moon className="w-6 h-6" />
          ) : (
            <Sun className="w-6 h-6" />
          )}
          <Switch
            checked={isDarkMode}
            onCheckedChange={toggleDarkMode}
            className={`${
              isDarkMode
                ? 'bg-indigo-600 focus:ring-indigo-500'
                : 'bg-gray-200 focus:ring-gray-500'
            }`}
          />
          {!isDarkMode ? (
            <Sun className="w-6 h-6" />
          ) : (
            <Moon className="w-6 h-6" />
          )}
        </div>
      </CardContent>
    </Card>
  );
};

export default DarkLightModeSwitch;
