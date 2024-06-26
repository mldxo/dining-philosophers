"""Main module for the dining philosophers problem"""

import random

from .dining_simulation import DiningSimulation

class DiningPhilosophers:
    """Main class for the dining philosophers problem"""
    
    def __init__(self) -> None:
        self.__dining_simulation : DiningSimulation | None = None
        self.__version : str | None = None
        self.__name : str | None = None
    
    @property
    def version(self) -> str:
        """Gets the version of the Dining simulation"""
        return self.__version
    
    @version.setter
    def version(self, version : str) -> None:
        """Sets the version of the Dining simulation"""
        self.__version = version
    
    @property
    def name(self) -> str:
        """Gets the name of the Dining simulation"""
        return self.__name
    
    @name.setter
    def name(self, name : str) -> None:
        """Sets the name of the Dining simulation"""
        self.__name = name

    @property
    def dining_simulation(self) -> DiningSimulation:
        """Gets the dining simulation"""
        return self.__dining_simulation
    
    @dining_simulation.setter
    def dining_simulation(self, dining_simulation : DiningSimulation) -> None:
        """Sets the dining simulation"""
        if dining_simulation is None:
            raise ValueError("Dining simulation cannot be None")
        if self.__dining_simulation is not None:
            del self.__dining_simulation
        self.__dining_simulation = dining_simulation

    def run_deterministic(self, n = 5, lambdas = [0.2, 0.3, 0.4, 0.5, 0.6], mi = 0.8, T = 100) -> None:
        """Runs the dining philosophers problem simulation with deterministic parameters"""
        print(f"Running {self.name} {self.version}")
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()

    def run_random(self) -> None:
        """Runs the dining philosophers problem simulation with random parameters"""
        print(f"Running {self.name} {self.version}")
        n = 5 # philosphers
        lambdas = [random.random() for _ in range(n)]
        mi = random.random()
        T = 100 # time steps
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()

    def run_showcase(self) -> None:
        """Runs the dining philosophers problem simulation multiple times showcasing the problem"""
        print(f"Running {self.name} {self.version}")
        n = 5 # philosphers
        lambdas = [0.4, 0.4, 0.4, 0.4, 0.4] # asking probabilities
        mi = 0.1 # stopping probability
        T = 100 # time steps
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()
        
        n = 5
        lambdas = [0.2, 0.2, 0.2, 0.2, 0.2]
        mi = 0.2
        T = 100
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()

        n = 5
        lambdas = [0.1, 0.1, 0.1, 0.1, 0.1]
        mi = 0.1
        T = 100
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()

        n = 5
        lambdas = [0.1, 0.2, 0.3, 0.4, 0.5]
        mi = 0.5
        T = 100
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()

        n = 5
        lambdas = [0.5, 0.4, 0.3, 0.2, 0.1]
        mi = 0.9
        T = 100
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()

        n = 5
        lambdas = [0.2, 0.3, 0.4, 0.5, 0.6]
        mi = 0.8
        T = 100
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()

        n = 5
        lambdas = [0.2, 0.3, 0.4, 0.5, 0.6]
        mi = 0.1
        T = 100
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()
        

        n = 5
        lambdas = [0.9, 0.1, 0.1, 0.1, 0.1]
        mi = 0.1
        T = 100
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()


        n = 5
        lambdas = [0.9, 0.1, 0.9, 0.1, 0.1]
        mi = 0.1
        T = 100
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()
        
        n = 5
        lambdas = [0.9, 0.1, 0.9, 0.1, 0.1]
        mi = 0.5
        T = 100
        self.dining_simulation = DiningSimulation(n, lambdas, mi, T)
        self.dining_simulation.simulate()
        self.dining_simulation.plot()