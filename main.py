import json
from classes.character import Character,Movement
from colorama import  Fore, Style


def validate_json(data: dict) -> bool:
    # Verificar la longitud máxima de movimientos
    for player in data.values():
        if "movimientos" in player:
            for mov in player["movimientos"]:
                if not len(mov) <= 5 :
                    return False
    # Verificar la longitud máxima de golpes
    for player in data.values():
        if "golpes" in player:
            for golpe in player["golpes"]:
                if not len(golpe) <= 1:
                    return False
    return True


def load_movements(data: dict, name: str) -> tuple:
    """
    Carga los movimientos y golpes del personaje desde los datos.

    Args:
        data (dict): Datos del personaje.
        name (str): Nombre del personaje.

    Returns:
        tuple: Tupla con los movimientos y golpes del personaje.
    """

    movements = data[name]["movimientos"]
    hits = data[name]["golpes"]
    return movements, hits


def choose_initial_player(movements_player_1: list, hits_player_1: list, movements_player_2: list, hits_player_2: list) -> int:
    """
    Elige el jugador inicial basado en el número total de combinaciones de movimientos y golpes.

    Args:
        movements_player_1 (list): Movimientos del jugador 1.
        hits_player_1 (list): Golpes del jugador 1.
        movements_player_2 (list): Movimientos del jugador 2.
        hits_player_2 (list): Golpes del jugador 2.

    Returns:
        int: Número del jugador que inicia la pelea.
    """

    sum_combinations_player_1 = len(movements_player_1) + len(hits_player_1)
    sum_combinations_player_2 = len(movements_player_2) + len(hits_player_2)

    if sum_combinations_player_1 < sum_combinations_player_2:
        return 1
    elif sum_combinations_player_1 > sum_combinations_player_2:
        return 2
    else:
        if len(movements_player_1) < len(movements_player_2):
            return 1
        elif len(movements_player_1) > len(movements_player_2):
            return 2
        else:
            if len(hits_player_1) < len(hits_player_2):
                return 1
            elif len(hits_player_1) > len(hits_player_2):
                return 2
            else:
                return 1


def start_battle(player_1: Character, player_2: Character, movements_player_1: str, hits_player_1: str,
                 movements_player_2: list, hits_player_2: list, initial_player: int) -> tuple:
    """
    Inicia la batalla entre dos jugadores y devuelve los eventos y el ganador.

    Args:
        player_1 (Character): Jugador 1.
        player_2 (Character): Jugador 2.
        movements_player_1 (list): Movimientos del jugador 1.
        hits_player_1 (list): Golpes del jugador 1.
        movements_player_2 (list): Movimientos del jugador 2.
        hits_player_2 (list): Golpes del jugador 2.
        initial_player (int): Jugador inicial.

    Retorna:
        tuple: Eventos de la batalla y el jugador ganador.
    """
    turn = 1  # Turnos
    events = []  #Almacena cada uno de los evento en una lista
    events.append("Descripción de la batalla")
    # Iniciar el ciclo hasta que alguno de los jugadores se quede sin puntos de vida
    while player_1.life_points > 0 or player_2.life_points > 0:
        # Empezar el turno en base al jugador inicial
        if initial_player == 1:
            # Jugador 1 realiza su combinación de movimiento y golpe
            if len(movements_player_1) > turn - 1:
                combination = [movements_player_1[turn - 1], hits_player_1[turn - 1]]
                player_1.attack(player_2, combination, events)
            if player_2.life_points <= 0:
                break
            # Jugador 2 realiza su combinación de movimiento y golpe
            if len(movements_player_2) > turn - 1:
                combination = [movements_player_2[turn - 1], hits_player_2[turn - 1]]
                player_2.attack(player_1, combination, events)
            if player_1.life_points <= 0 or player_2.life_points <= 0:
                break
            # Si la cantidad de movimientos ingresados del player_2 iguala al numero de turnos
            if len(movements_player_2)==turn:
                break
        else:
            # Jugador 2 realiza su combinación de movimiento y golpe
            if len(movements_player_2) > turn - 1:
                combination = [movements_player_2[turn - 1], hits_player_2[turn - 1]]
                player_2.attack(player_1, combination, events)
            if player_1.life_points <= 0:
                break
            # Jugador 1 realiza su combinación de movimiento y golpe
            if len(movements_player_1) > turn - 1:
                combination = [movements_player_1[turn - 1], hits_player_1[turn - 1]]
                player_1.attack(player_2, combination, events)
            if player_1.life_points <= 0 or player_2.life_points <= 0:
                break
            # Si la cantidad de movimientos ingresados del player_1 iguala al numero de turnos
            if len(movements_player_1)==turn:
                break
        turn += 1

    return events, player_1 if player_1.life_points > player_2.life_points else player_2 


def main():
    with open('data/test_1.json', 'r') as file:
        # Cargar los datos JSON desde el archivo
        data = json.load(file)
        # Valida que la data sea correcta
        if not validate_json(data):
            print("El archivo cargado no es válido.")
        else:
            # Cargar los movimientos y golpes de los jugadores
            movements_player_1, hits_player_1 = load_movements(data, "player1")
            movements_player_2, hits_player_2 = load_movements(data, "player2")

            movements_player_1_base = [
                Movement("Taladoken", 3, "DSDP", "special"),
                Movement("Remuyuken", 2, "SDK", "special"),
                Movement("Puño", 1, "P", "basic"),
                Movement("Patada", 1, "K", "basic")
            ]

            movements_player_2_base = [
                Movement("Remuyuken", 3, "SAK", "special"),
                Movement("Taladoken", 2, "ASAP", "special"),
                Movement("Puño", 1, "P", "basic"),
                Movement("Patada", 1, "K", "basic")
            ]

            # Crear los objetos de los jugadores
            player_1 = Character("Tonyn", 6, movements_player_1_base,Fore.BLUE)
            player_2 = Character("Arnaldor", 6, movements_player_2_base,Fore.GREEN)

            # Elegir el jugador inicial
            initial_player = choose_initial_player(movements_player_1, hits_player_1, movements_player_2, hits_player_2)

            # Iniciar la batalla entre los jugadores
            events, winner = start_battle(player_1, player_2, movements_player_1, hits_player_1, movements_player_2,
                                        hits_player_2, initial_player)

            winner_life_points = winner.life_points

            events.append(f"Resultado : {winner} gana la pelea y aún le quedan {winner_life_points} puntos de vida.")

            # Mostrar los eventos de la batalla en la consola
            for event in events:
                print(event)


if __name__ == "__main__":
    main()
