import React, { Suspense } from "react";
import Navbar from "../components/Navbar";
import Articles from "../components/Articles";
import TruncatedArticles from "@/components/TruncatedArticles";

export default function Home(): JSX.Element {
  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      <main className="container px-4 mx-auto">
        <section className="py-20 flex flex-col items-center text-center">
          <div className="space-y-4 max-w-3xl">
            <h1 className="text-4xl md:text-6xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500">
              We are all doomed...
            </h1>
            <p className="text-xl text-muted-foreground">
              See all the most pessimistic news articles in one place.
            </p>
            <div className="flex gap-4 justify-center mt-4">
              <a href="#articles" className="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2">
                Browse Articles
              </a>
              {/* <a href="/about" className="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input hover:bg-accent hover:text-accent-foreground h-10 px-4 py-2">
                About Us
              </a> */}
            </div>
          </div>
        </section>

        <div id="articles">
          <Suspense fallback={<div>Loading...</div>}>
            <TruncatedArticles />
            <div className="flex justify-center py-6"> {/* Center and add padding */}
              <a
                href="/articles"
                className="inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-6 py-3" // Added px-6 and py-3 for padding
              >
                See More
              </a>
            </div>
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