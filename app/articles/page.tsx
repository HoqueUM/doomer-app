import React, { Suspense } from "react";
import Navbar from "@/components/Navbar";
import Articles from "@/components/Articles";

export default function Page(): JSX.Element {
    return (
      <div className="min-h-screen bg-background">
        <Navbar />
        <main className="container px-4 mx-auto">
          <div id="articles">
            <Suspense fallback={<div>Loading...</div>}>
              <Articles />
            </Suspense>
          </div>
        </main>
        
        <footer className="border-t py-6 md:py-10">
          <div className="container px-4 mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
            <div className="flex items-center gap-2">
              <div className="h-6 w-6 rounded-md bg-gradient-to-br from-blue-500 to-purple-600"></div>
              <span className="font-semibold">doomer.space</span>
            </div>
            {/* <div className="flex gap-6">
              <a href="/terms" className="text-sm text-muted-foreground hover:text-foreground">Terms</a>
              <a href="/privacy" className="text-sm text-muted-foreground hover:text-foreground">Privacy</a>
              <a href="/contact" className="text-sm text-muted-foreground hover:text-foreground">Contact</a>
            </div> */}
            <div className="text-sm text-muted-foreground">
              © 2025 doomer.space. All rights reserved.
            </div>
          </div>
        </footer>
      </div>
    );
  }