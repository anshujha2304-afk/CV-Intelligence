import Navbar from "../components/Navbar";

function Home() {
  return (
    <>
      <Navbar />

      <main className="min-h-screen bg-slate-100 flex items-center justify-center px-8">
        <div className="text-center max-w-3xl">
          <h1 className="text-6xl font-extrabold text-blue-600">
            AI Resume Intelligence
          </h1>

          <p className="mt-6 text-xl text-gray-600">
            Upload your resume, get an ATS score, AI-powered feedback,
            job matching, and resume improvements — all in one place.
          </p>

          <div className="mt-10 flex justify-center gap-5">
            <button className="bg-blue-600 text-white px-8 py-3 rounded-xl hover:bg-blue-700 transition">
              Get Started
            </button>

            <button className="border border-blue-600 text-blue-600 px-8 py-3 rounded-xl hover:bg-blue-50 transition">
              Learn More
            </button>
          </div>
        </div>
      </main>
    </>
  );
}

export default Home;