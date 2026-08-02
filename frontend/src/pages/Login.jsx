function Login() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <div className="bg-white p-10 rounded-xl shadow-lg w-96">
        <h1 className="text-3xl font-bold text-center text-blue-600">
          Login
        </h1>

        <input
          type="email"
          placeholder="Email"
          className="w-full border p-3 mt-6 rounded-lg"
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full border p-3 mt-4 rounded-lg"
        />

        <button className="w-full bg-blue-600 text-white p-3 rounded-lg mt-6 hover:bg-blue-700">
          Login
        </button>
      </div>
    </div>
  );
}

export default Login;