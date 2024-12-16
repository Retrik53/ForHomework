# Класс питания
class PowerSupply:
    def supply_power(self):
        print("Питание подключено.")


# Класс материнской платы
class Motherboard:
    def distribute_power(self):
        print("Напряжение перераспределено.")


# Класс центрального процессора (CPU)
class CPU(PowerSupply, Motherboard):  # Множественное наследование
    def __init__(self, frequency, cores):
        self.frequency = frequency
        self.cores = cores

    def activate_turbo_mode(self):
        print("Активируем ускоренный режим.")


# Класс оперативной памяти (RAM)
class RAM(Motherboard):  # Множественное наследование
    def __init__(self, memory_size, memory_frequency):
        self.memory_size = memory_size
        self.memory_frequency = memory_frequency

    def load_data(self):
        print("Загружаем данные в оперативную память.")

    def unload_data(self):
        print("Выгружаем данные из оперативной памяти.")


# Класс твердотельного накопителя (SSD)
class SSD(Motherboard):  # Множественное наследование
    def __init__(self, storage_capacity):
        self.storage_capacity = storage_capacity

    def save_data(self):
        print("Сохраняем данные на SSD.")

    def delete_data(self):
        print("Удаляем данные с SSD.")


# Класс графического процессора (GPU)
class GPU(Motherboard):  # Множественное наследование
    def __init__(self, model, video_memory):
        self.model = model
        self.video_memory = video_memory

    def display_image(self):
        print("Выводим изображение на экран.")


# Класс компьютера
class Computer(CPU, RAM, SSD, GPU):  # Множественное наследование
    def __init__(
            self,
            power_supply: PowerSupply,
            motherboard: Motherboard,
            cpu: CPU,
            ram: RAM,
            ssd: SSD,
            gpu: GPU
    ):
        self.power_supply = power_supply
        self.motherboard = motherboard
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.gpu = gpu

    def start(self):
        # Подключаем питание
        self.power_supply.supply_power()

        # Перераспределяем напряжение
        self.motherboard.distribute_power()

        # Активируем турбо режим процессора
        self.cpu.activate_turbo_mode()

        # Загружаем данные в оперативную память
        self.ram.load_data()

        # Сохраняем данные на SSD
        self.ssd.save_data()

        # Выводим изображение на экран
        self.gpu.display_image()


# Создаем объекты компонентов
power_supply = PowerSupply()
motherboard = Motherboard()
cpu = CPU(4.0, 8)
ram = RAM(16, 3200)
ssd = SSD(512)
gpu = GPU('RTX 3080', 10)

# Создаем объект компьютера
computer = Computer(power_supply, motherboard, cpu, ram, ssd, gpu)

# Запускаем компьютер
computer.start()