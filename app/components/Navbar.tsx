"use client";
import { useState } from 'react'

export default function Home() {
  const [showNavbar, setShowNavbar] = useState(false)
  
  const handleShowNavbar = () => {
    setShowNavbar(!showNavbar)
  }
  
  return (
    <div className="flex flex-col pb-4">
      <nav className="fixed top-0 left-0 right-0 w-full px-8 shadow-sm shadow-neutral-500 h-16 flex items-center bg-black z-50">
        <div className="container flex justify-between items-center">
          <a href="/">
            <div className="logo font-bold">
              doomer.space
            </div>
          </a>
        </div>
      </nav>
      
      <div className="h-16"></div>
    </div>
  )
}
