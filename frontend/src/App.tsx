/**
 * Main App component with routing
 */

import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import LoginForm from './components/auth/LoginForm';
import ResidentList from './components/residents/ResidentList';
import Header from './components/layout/Header';
import { authService } from './api/auth';

const PrivateRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return authService.isAuthenticated() ? <>{children}</> : <Navigate to="/login" />;
};

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginForm />} />
        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <div>
                <Header />
                <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
                  <h2 className="text-2xl font-semibold">Dashboard</h2>
                  <p className="mt-2 text-gray-600">Welcome to RMC Manager</p>
                </div>
              </div>
            </PrivateRoute>
          }
        />
        <Route
          path="/residents"
          element={
            <PrivateRoute>
              <div>
                <Header />
                <ResidentList />
              </div>
            </PrivateRoute>
          }
        />
        <Route path="/" element={<Navigate to="/dashboard" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
