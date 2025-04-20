import React, { useState } from 'react';
import axios from 'axios';

function Auth() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async () => {
    try {
      const response = await axios.post('/auth/login', { username, password });
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Login failed');
    }
  };

  const handleRegister = async () => {
    try {
      const response = await axios.post('/auth/register', { username, password });
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Registration failed');
    }
  };

  return (
    <div>
      <h2>Auth Page</h2>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
      <button onClick={handleRegister}>Register</button>
      <p>{message}</p>
    </div>
  );
}

export default Auth;
