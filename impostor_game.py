import { useState } from "react";
import { Button } from "@/components/ui/button";

// Lista de jugadores actualizada cargada del archivo
const jugadores = [
  "Lamine Yamal", "Erling Haaland", "Vinícius Júnior", "Kylian Mbappé", "Jude Bellingham",
  "Bukayo Saka", "Florian Wirtz", "Jamal Musiala", "Phil Foden", "Cole Palmer",
  "Federico Valverde", "Pedri", "João Neves", "Khvicha Kvaratskhelia", "Rodri Hernández",
  "Gavi", "Alejandro Garnacho", "Martin Ødegaard", "Declan Rice", "Rafael Leão",
  "Lautaro Martínez", "Raphinha", "Josko Gvardiol", "Eduardo Camavinga", "Aurélien Tchouaméni",
  "Frenkie de Jong", "Ousmane Dembélé", "Mohamed Salah", "Harry Kane", "Kevin De Bruyne",
  "Bernardo Silva", "Bruno Fernandes", "Darwin Núñez", "Marcus Rashford", "Jadon Sancho",
  "Lisandro Martínez", "Virgil van Dijk", "Trent Alexander-Arnold", "Andy Robertson", "Alisson Becker",
  "Ederson Moraes", "Manuel Neuer", "Marc-André ter Stegen", "Mike Maignan", "Gianluigi Donnarumma",
  "Gregor Kobel", "William Saliba", "Alessandro Bastoni", "Gabriel Magalhães", "Marquinhos",
  "Achraf Hakimi", "Theo Hernández", "Dani Carvajal", "Ronald Araújo", "Jules Koundé",
  "Eder Militão", "Antonio Rüdiger", "Dayot Upamecano", "Matthijs de Ligt", "Milan Skriniar",
  "Ruben Dias", "Aymeric Laporte", "Pau Torres", "Benjamin Pavard", "Alphonso Davies",
  "Nuno Mendes", "Ferland Mendy", "João Cancelo", "Dani Olmo", "Marco Asensio",
  "Nicolo Barella", "Sandro Tonali", "Manuel Locatelli", "Sergej Milinković-Savić", "Adrien Rabiot",
  "Mateo Kovačić", "Ilkay Gündogan", "Luka Modrić", "Toni Kroos", "Casemiro",
  "Thomas Partey", "Kai Havertz", "Christopher Nkunku", "Kingsley Coman", "Leroy Sané",
  "Serge Gnabry", "Jamal Musiala", "Joshua Kimmich", "Leon Goretzka", "Florian Wirtz",
  "Antoine Griezmann", "Álvaro Morata", "Ferran Torres", "Ansu Fati", "Memphis Depay",
  "Paulo Dybala", "Ángel Di María", "Neymar Jr.", "Lionel Messi", "Cristiano Ronaldo"
];

export default function Game() {
  const [round, setRound] = useState(0);
  const [roles, setRoles] = useState<Array<{ name: string; role: string }>>([]);
  const [showRole, setShowRole] = useState(false);

  // Configurables por el usuario
  const [numJugadores, setNumJugadores] = useState(5);
  const [numImpostores, setNumImpostores] = useState(1);
  const total = numJugadores + numImpostores;
  const configInvalida = numImpostores < 1 || numJugadores < 1 || numImpostores >= total;

  const startGame = () => {
    // Elegir un jugador al azar que será el mismo para todos los "Jugador"
    const chosenPlayer = jugadores[Math.floor(Math.random() * jugadores.length)];

    // Crear N jugadores (mismo nombre) y M impostores
    let roundRoles: Array<{ name: string; role: string }> = [];
    for (let i = 0; i < numJugadores; i++) roundRoles.push({ name: chosenPlayer, role: "Jugador" });
    for (let i = 0; i < numImpostores; i++) roundRoles.push({ name: "Impostor", role: "Impostor" });

    // Mezclar
    roundRoles = roundRoles.sort(() => Math.random() - 0.5);

    setRoles(roundRoles);
    setRound(0);
    setShowRole(false);
  };

  const nextStep = () => {
    if (round < roles.length) {
      setShowRole(!showRole);
      if (showRole) setRound((r) => r + 1);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-black text-white gap-6 p-4">
      {roles.length === 0 ? (
        <>
          <h1 className="text-2xl font-bold">Juego de Impostores</h1>

          {/* Controles de configuración */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full max-w-md">
            <label className="flex flex-col gap-2">
              <span className="text-sm text-gray-300">Cantidad de jugadores (normal)</span>
              <input
                type="number"
                min={1}
                value={numJugadores}
                onChange={(e) => setNumJugadores(parseInt(e.target.value || "0"))}
                className="bg-gray-800 text-white px-3 py-2 rounded-lg"
              />
            </label>

            <label className="flex flex-col gap-2">
              <span className="text-sm text-gray-300">Cantidad de impostores</span>
              <input
                type="number"
                min={1}
                value={numImpostores}
                onChange={(e) => setNumImpostores(parseInt(e.target.value || "0"))}
                className="bg-gray-800 text-white px-3 py-2 rounded-lg"
              />
            </label>
          </div>

          {configInvalida && (
            <p className="text-red-400 text-sm -mt-2">
              Configuración inválida: impostores &lt; total y ambos mayores a 0.
            </p>
          )}

          <Button onClick={startGame} className="px-6 py-3 text-lg rounded-2xl" disabled={configInvalida}>
            Iniciar Juego ({total} personas)
          </Button>
        </>
      ) : round >= roles.length ? (
        <>
          <h2 className="text-xl">Fin del Juego 🎉</h2>
          <Button onClick={() => setRoles([])}>Nueva configuración</Button>
          <Button onClick={startGame} className="mt-2">Reiniciar con misma configuración</Button>
        </>
      ) : (
        <>
          {!showRole ? (
            <>
              <div className="w-64 h-64 bg-black border border-gray-600 rounded-2xl flex items-center justify-center">
                <span className="text-gray-500">Pantalla Negra</span>
              </div>
              <div className="text-sm text-gray-400">Turno {round + 1} de {roles.length}</div>
              <Button onClick={nextStep}>Siguiente</Button>
            </>
          ) : (
            <>
              <div className="w-64 h-64 bg-gray-800 rounded-2xl flex flex-col items-center justify-center text-xl font-bold p-4 text-center">
                <p>{roles[round].name}</p>
                <p className="mt-2 text-lg">{roles[round].role}</p>
              </div>
              <div className="text-sm text-gray-400">Turno {round + 1} de {roles.length}</div>
              <Button onClick={nextStep}>Siguiente</Button>
            </>
          )}
        </>
      )}
    </div>
  );
}
