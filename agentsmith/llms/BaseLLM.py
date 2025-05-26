from agentsmith.core.runnable import Runnable, Input, Output
from abc import ABC, abstractmethod
from typing import Iterator, AsyncIterator, Optional
import asyncio

class BaseLLM(Runnable[Input, Output], ABC):
    @abstractmethod
    def run(self, prompt : Input) -> Output:
        pass
    
    @abstractmethod
    async def arun(self, prompt : Input) -> Output:
        pass
        
    def stream(self, prompt : Input) -> Iterator[Output]:
        return self.run(prompt)
    
    async def astream(self, prompt : Input) -> AsyncIterator[Output]:
        async for output in self.arun(prompt = prompt):
            yield output
        
    