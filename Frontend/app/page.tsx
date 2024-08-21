"use client"; 

import { useEffect, useState } from "react";
import axios from "axios";
import { Ascent } from "./types";

const AscentsPage = () => {
  const [ascents, setAscents] = useState<Ascent[]>([]);

  useEffect(() => {
    const fetchAscents = async () => {
      try {
        const response = await axios.get<Ascent[]>("http://localhost:8000/encadenes/api/v1/", {withCredentials: true});
        setAscents(response.data);
      } catch (error) {
        console.error("Error fetching ascents:", error);
      }
    };

    fetchAscents();
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Lista de Ascensos</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {ascents.map((ascent) => (
          <div key={ascent.name} className="bg-white shadow-md rounded-lg p-4">
            <h2 className="text-red-500 text-3xl font-bold mb-4">{ascent.name}</h2>
            <p><strong>Grado:</strong> {ascent.grado}</p>
            <p><strong>Rating:</strong> {ascent.rating}</p>
            <p><strong>Total Ascensos:</strong> {ascent.total_ascents}</p>
            <p><strong>Recomendado por:</strong> {ascent.recommended_by}</p>
            <p><strong>Sector:</strong> {ascent.sector}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AscentsPage;
