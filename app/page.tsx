import Navbar from "./components/Navbar"
import Articles from "./components/Articles"

export default function Home() {
  return (
    <main className="px-4 sm:px-8 pb-4 max-w-[75rem] mx-auto">
      <Navbar />
      <Articles />
    </main>
  )
}
