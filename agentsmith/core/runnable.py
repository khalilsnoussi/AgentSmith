from typing import Generic, TypeVar, Iterator, AsyncIterator
from abc import ABC, abstractmethod

Input = TypeVar("Input", contravariant=True)
Output = TypeVar("Output", covariant=True)




class Runnable(Generic[Input, Output], ABC):
    """_summary_

    Args:
        Generic (_type_): _description_
        ABC (_type_): _description_
    """
    @property
    def InputType(self) -> type[Input]:
        """returns type of Input 

        Returns:
            Input: _description_
        """
        return
    
    @property
    def OutputType(self) -> type[Output]:
        """return the type of Output 

        Returns:
            Output: _description_
        """
        return
    
    @abstractmethod
    def run(self, input : Input) -> Output:
        """Runs the runnable and transforms input of type Input into Output. 

        Args:
            input (Input): _description_

        Returns:
            Output: _description_
        """
        
    @abstractmethod
    async def arun(self, input : Input) -> Output:
        """runs the runnable asynchronously and transforms input of type Input into an output of type Output.

        Args:
            input (Input): _description_

        Returns:
            Output: _description_
        """
        yield await self.run(input = input)
    
    @abstractmethod
    def stream(self, input : Input) -> Iterator[Output]:
        """_summary_

        Args:
            input (Input): _description_

        Returns:
            Output: _description_
        """
        
    @abstractmethod
    async def astream(self, input : Input) -> AsyncIterator[Output]:
        """_summary_

        Args:
            input (Input): _description_

        Yields:
            Iterator[Output]: _description_
        """
        