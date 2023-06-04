from colorama import  Fore, Style

class Movement:
    def __init__(self, name:str, damage:int, command:str, type:str):
        self.name = name  # Nombre del movimiento
        self.damage = damage  # Daño
        self.command = command # Comandos
        self.type = type # Tipo de movimiento (básico o especial)

    def __str__(self) -> str:
        return self.name
    
class Character:
    def __init__(self, name:str, life_points:int, movements:list[Movement],color:Fore):
        self.name = name  # Nombre del personaje
        self.life_points = life_points  # Puntos de vida
        self.movements = movements  # Lista de objetos Movement
        self.color = color # Color del personaje

    def __str__(self) -> str:
        return self.name
    
    def get_movements_description(self, string: str, events: list) -> None:
        # Diccionario que mapea las letras de botones
        actions = {
            "W": "hacia arriba",
            "S": "hacia abajo",
            "A": "hacia atrás",
            "D": "hacia adelante"
        }

        # Inicializar variables
        result = f"- {self.name} se mueve " if string != "" else f"- {self.name}"
        prev_letter = None
        count = 0

        # Iterar sobre cada letra en la cadena de movimientos
        for letter in string:
            # Si la letra actual es diferente a la anterior
            if letter != prev_letter:
                if prev_letter is not None and prev_letter in actions:
                    action = actions[prev_letter]
                    count_str = f" {count} vez" if count == 1 else f"{count} veces"
                    result += f"{count_str} {action}, "

                # Reiniciar el contador de ocurrencias
                count = 1
            else:
                # Si la letra actual es igual a la anterior, incrementar el contador
                count += 1
            # Asignar la tra actual como la anterior
            prev_letter = letter

        # Procesar el último grupo de letras
        if prev_letter is not None and prev_letter in actions:
            action = actions[prev_letter]
            count_str = f"{count} vez" if count == 1 else f"{count} veces"
            result += f"{count_str} {action} {'' if count==1 else ','} "

        # Agregar el resultado a la lista de eventos
        events.append(result)

    def update_life_points(self,damage:int)->None:
        self.life_points -= damage
        if self.life_points <= 0:
            self.life_points = 0
        pass

    def attack(self, opponent:"Character", combination:list, events:list) -> None:
        movements ,hits= combination # Secuencia de movimientos
        last_event_index = len(events) - 1

        # Almacenar los movimientos de tipo especial y básico en listas separadas
        special_moves = [m for m in self.movements if m.type == "special"]
        basic_moves = [m for m in self.movements if m.type == "basic"]
        
        # Buscar algún movimiento especial en la combinación ingresada
        for move in special_moves:
            combination = movements + hits
            if move.command in combination:
                new_temp = combination.replace(move.command, "")
                if new_temp:
                    last_event_index = len(events) - 1
                    self.get_movements_description(new_temp, events)
                    events[last_event_index] += f"y conecta un {move.name}"
                else:
                    events.append(f"- {self.name} conecta un {move.name}")
                opponent.update_life_points(move.damage)
                last_event_index = len(events) - 1
                events[last_event_index] += f".{opponent.color} Le quedan {opponent.life_points} de vida a {opponent}.{Style.RESET_ALL}"

                return
        # Si no encuentra movimientos especiales, crea los eventos solo de movimientos
        self.get_movements_description(movements, events)

        #Obtener último indice de los eventos
        last_event_index = len(events) - 1

        # Almacenar el último evento registrado en temp
        temp = events[last_event_index]
        
        # Buscar si se ingresó algún movimiento básico en la combinación de golpes
        for move in basic_moves:
            if hits == move.command:
                event = f" y le da un {move} a {opponent}"
                if movements == "":
                    event = event.replace(" y", "")
                temp += event
                # Reducir los puntos de vida del oponente
                opponent.update_life_points(move.damage)

                break

        # Actualizar el último evento con la variable temp
        events[last_event_index] = temp
        events[last_event_index]+=f"{opponent.color} . Le quedan {opponent.life_points} de vida a {opponent}.{Style.RESET_ALL}"
