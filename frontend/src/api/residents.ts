/**
 * Residents API service
 */

import apiClient, { PaginatedResponse } from './client';

export interface Resident {
  id: string;
  first_name: string;
  last_name: string;
  date_of_birth: string | null;
  diet_type: string | null;
  iddsi_level: string | null;
  meal_size: string;
  fluid_restriction_ml: number | null;
  room: string | null;
  wing: string | null;
  is_active: boolean;
  allergies: Allergy[];
}

export interface Allergy {
  id: string;
  allergen: string;
  severity: string | null;
  is_hard_restriction: boolean;
}

export interface CreateResidentData {
  first_name: string;
  last_name: string;
  date_of_birth?: string;
  diet_type?: string;
  iddsi_level?: string;
  meal_size?: string;
  room?: string;
  wing?: string;
}

class ResidentsService {
  async getAll(params?: { wing?: string; search?: string }): Promise<PaginatedResponse<Resident>> {
    const response = await apiClient.get<PaginatedResponse<Resident>>('/residents/', { params });
    return response.data;
  }

  async getById(id: string): Promise<Resident> {
    const response = await apiClient.get<Resident>(`/residents/${id}/`);
    return response.data;
  }

  async create(data: CreateResidentData): Promise<Resident> {
    const response = await apiClient.post<Resident>('/residents/', data);
    return response.data;
  }

  async update(id: string, data: Partial<CreateResidentData>): Promise<Resident> {
    const response = await apiClient.patch<Resident>(`/residents/${id}/`, data);
    return response.data;
  }

  async delete(id: string): Promise<void> {
    await apiClient.delete(`/residents/${id}/`);
  }
}

export const residentsService = new ResidentsService();
export default residentsService;
