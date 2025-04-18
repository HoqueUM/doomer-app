"use client";

import { useState } from "react";
import { Menu, X } from "lucide-react";
import { ThemeToggle } from "./ThemeToggle";
import { Button } from "@/components/ui/button";

export default function Navbar(): JSX.Element {
  const [isOpen, setIsOpen] = useState<boolean>(false);

  return (
    <nav className="border-b bg-background/95 backdrop-blur supports-backdrop-blur:bg-background/60 sticky top-0 z-50 w-full">
      <div className="flex h-16 items-center px-4 justify-between">
        <div className="flex items-center gap-2">
          <a href="/" className="flex items-center">
            <div className="h-8 w-8 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600 mr-2"></div>
            <span className="font-bold text-xl bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-purple-600">
              doomer.space
            </span>
          </a>
        </div>

        {/* Desktop navigation */}
        <div className="hidden md:flex items-center gap-6">
          <div className="flex items-center gap-6">
            {/* <a href="/features" className="text-sm font-medium hover:text-primary transition-colors">
              Features
            </a>
            <a href="/pricing" className="text-sm font-medium hover:text-primary transition-colors">
              Pricing
            </a>
            <a href="/docs" className="text-sm font-medium hover:text-primary transition-colors">
              Documentation
            </a>
            <a href="/blog" className="text-sm font-medium hover:text-primary transition-colors">
              Blog
            </a> */}
          </div>
          <div className="flex items-center gap-2">
            <ThemeToggle />
            {/* <Button variant="ghost" size="sm">
              Log In
            </Button>
            <Button size="sm">Sign Up</Button> */}
          </div>
        </div>

        {/* Mobile menu button */}
        <button
          className="md:hidden p-2 rounded-md"
          onClick={() => setIsOpen(!isOpen)}
        >
          {isOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {/* Mobile navigation */}
      {isOpen && (
        <div className="md:hidden p-4 space-y-4 border-t">
          <a href="/features" className="block py-2 text-sm font-medium hover:text-primary transition-colors">
            Features
          </a>
          <a href="/pricing" className="block py-2 text-sm font-medium hover:text-primary transition-colors">
            Pricing
          </a>
          <a href="/docs" className="block py-2 text-sm font-medium hover:text-primary transition-colors">
            Documentation
          </a>
          <a href="/blog" className="block py-2 text-sm font-medium hover:text-primary transition-colors">
            Blog
          </a>
          <div className="flex items-center justify-between pt-4 border-t">
            <ThemeToggle />
            <div className="space-x-2">
              <Button variant="ghost" size="sm">
                Log In
              </Button>
              <Button size="sm">Sign Up</Button>
            </div>
          </div>
        </div>
      )}
    </nav>
  );
}