"use client";

import { useState } from "react";
import { ThemeToggle } from "./ThemeToggle";
import { ThemeAwareLogo } from "@/components/ThemeAwareLogo";

export default function Navbar(): JSX.Element {
  return (
    <nav className="border-b bg-background/95 backdrop-blur supports-backdrop-blur:bg-background/60 sticky top-0 z-50 w-full">
      <div className="flex h-16 items-center px-4 justify-between">
        <div className="flex items-center">
          <a href="/" className="flex items-center">
            <div>
              <ThemeAwareLogo />
            </div>
            <span className="font-bold text-xl">
              doomer.space
            </span>
          </a>
        </div>

        {/* Desktop navigation */}
        <div className="hidden md:flex items-center gap-6">
          <div className="flex items-center gap-2">
            <ThemeToggle />
          </div>
        </div>

        {/* Mobile: Only theme toggle */}
        <div className="md:hidden">
          <ThemeToggle />
        </div>
      </div>
    </nav>
  );
}