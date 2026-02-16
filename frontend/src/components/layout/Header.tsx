/**
 * Application header component
 */

import React from 'react';
import { useNavigate } from 'react-router-dom';
import { authService } from '../../api/auth';

export const Header: React.FC = () => {
  const navigate = useNavigate();
  const user = authService.getStoredUser();

  const handleLogout = async () => {
    await authService.logout();
    navigate('/login');
  };

  return (
    <header className="bg-white shadow">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center py-6">
          <div className="flex items-center">
            <h1 className="text-3xl font-bold text-gray-900">RMC Manager</h1>
          </div>

          <div className="flex items-center space-x-4">
            {user && (
              <>
                <div className="text-sm">
                  <p className="font-medium text-gray-700">
                    {user.first_name} {user.last_name}
                  </p>
                  <p className="text-gray-500">{user.role}</p>
                </div>
                <button
                  onClick={handleLogout}
                  className="px-4 py-2 text-sm font-medium text-gray-700 hover:text-gray-900"
                >
                  Logout
                </button>
              </>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
