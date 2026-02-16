/**
 * Meal order form component
 */

import React, { useState } from 'react';

interface MealOrderFormProps {
  residentId: string;
  residentName: string;
  onSubmit: (data: any) => void;
  onCancel: () => void;
}

export const MealOrderForm: React.FC<MealOrderFormProps> = ({
  residentId,
  residentName,
  onSubmit,
  onCancel,
}) => {
  const [mainCourse, setMainCourse] = useState('');
  const [soup, setSoup] = useState('');
  const [dessert, setDessert] = useState('');
  const [beverage, setBeverage] = useState('');
  const [notes, setNotes] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      resident_id: residentId,
      main_course: mainCourse,
      soup,
      dessert,
      beverage,
      notes,
    });
  };

  return (
    <div className="bg-white shadow rounded-lg p-6">
      <div className="mb-4">
        <h2 className="text-xl font-semibold text-gray-900">
          Meal Order for {residentName}
        </h2>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Main Course
          </label>
          <select
            className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
            value={mainCourse}
            onChange={(e) => setMainCourse(e.target.value)}
            required
          >
            <option value="">Select main course</option>
            <option value="roast_chicken">Roast Chicken</option>
            <option value="fish_fillet">Fish Fillet</option>
            <option value="beef_stew">Beef Stew</option>
            <option value="vegetarian_pasta">Vegetarian Pasta</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">
            Soup
          </label>
          <select
            className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
            value={soup}
            onChange={(e) => setSoup(e.target.value)}
          >
            <option value="">No soup</option>
            <option value="pumpkin">Pumpkin Soup</option>
            <option value="chicken">Chicken Soup</option>
            <option value="vegetable">Vegetable Soup</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">
            Dessert
          </label>
          <select
            className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
            value={dessert}
            onChange={(e) => setDessert(e.target.value)}
          >
            <option value="">No dessert</option>
            <option value="ice_cream">Ice Cream</option>
            <option value="fruit_salad">Fruit Salad</option>
            <option value="pudding">Pudding</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">
            Beverage
          </label>
          <select
            className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
            value={beverage}
            onChange={(e) => setBeverage(e.target.value)}
          >
            <option value="">No beverage</option>
            <option value="water">Water</option>
            <option value="juice">Juice</option>
            <option value="tea">Tea</option>
            <option value="coffee">Coffee</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">
            Special Instructions
          </label>
          <textarea
            rows={3}
            className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            placeholder="Any special instructions or modifications..."
          />
        </div>

        <div className="flex justify-end space-x-3">
          <button
            type="button"
            onClick={onCancel}
            className="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50"
          >
            Cancel
          </button>
          <button
            type="submit"
            className="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700"
          >
            Submit Order
          </button>
        </div>
      </form>
    </div>
  );
};

export default MealOrderForm;
