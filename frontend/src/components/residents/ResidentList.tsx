/**
 * Resident list component
 */

import React, { useEffect, useState } from 'react';
import { residentsService, Resident } from '../../api/residents';

export const ResidentList: React.FC = () => {
  const [residents, setResidents] = useState<Resident[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadResidents();
  }, [searchTerm]);

  const loadResidents = async () => {
    try {
      setLoading(true);
      const data = await residentsService.getAll({ search: searchTerm });
      setResidents(data.results);
    } catch (err: any) {
      setError('Failed to load residents');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-gray-900">Residents</h1>
        <button className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700">
          Add Resident
        </button>
      </div>

      <div className="mb-4">
        <input
          type="text"
          placeholder="Search residents..."
          className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      {error && (
        <div className="bg-red-50 text-red-800 p-4 rounded-md mb-4">
          {error}
        </div>
      )}

      {loading ? (
        <div className="text-center py-8">Loading...</div>
      ) : (
        <div className="bg-white shadow overflow-hidden sm:rounded-md">
          <ul className="divide-y divide-gray-200">
            {residents.map((resident) => (
              <li key={resident.id}>
                <div className="px-4 py-4 sm:px-6 hover:bg-gray-50 cursor-pointer">
                  <div className="flex items-center justify-between">
                    <div className="flex-1">
                      <p className="text-sm font-medium text-indigo-600">
                        {resident.first_name} {resident.last_name}
                      </p>
                      <div className="mt-2 flex items-center text-sm text-gray-500">
                        <span>Diet: {resident.diet_type || 'N/A'}</span>
                        <span className="mx-2">•</span>
                        <span>IDDSI: {resident.iddsi_level || 'N/A'}</span>
                        <span className="mx-2">•</span>
                        <span>Size: {resident.meal_size}</span>
                      </div>
                      {resident.allergies && resident.allergies.length > 0 && (
                        <div className="mt-2">
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800">
                            {resident.allergies.length} Allergies
                          </span>
                        </div>
                      )}
                    </div>
                    <div>
                      <span className={`px-2 py-1 text-xs rounded-full ${
                        resident.is_active 
                          ? 'bg-green-100 text-green-800' 
                          : 'bg-gray-100 text-gray-800'
                      }`}>
                        {resident.is_active ? 'Active' : 'Inactive'}
                      </span>
                    </div>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ResidentList;
