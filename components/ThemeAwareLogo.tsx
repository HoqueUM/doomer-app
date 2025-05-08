"use client";

import Image from "next/image";
import { useTheme } from "next-themes";
import { useEffect, useState } from "react";

export function ThemeAwareLogo() {
  const { resolvedTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  
  useEffect(() => {
    setMounted(true);
  }, []);
  
  if (!mounted) {
    return (
      <div className="h-8 w-8 rounded-lg bg-gray-200 dark:bg-gray-700" />
    );
  }

  const logoSrc = resolvedTheme === "dark" 
    ? "/doomer_logo_light.png" 
    : "/doomer_logo_dark.png";
  
  return (
    <div className="h-8 w-8 rounded-lg flex-shrink-0 flex items-center justify-center">
      <Image
        src={logoSrc}
        alt="Logo"
        width={32}
        height={32}
        className="rounded-lg"
      />
    </div>
  );
}