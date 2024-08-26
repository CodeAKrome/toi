import random
import string
import json
from dataclasses import dataclass, field, asdict

def generate_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=12))

# frozen doesn't allow changes after object creation
#@dataclass(frozen=True)
# kwonly forbids positional arguments for creation
#@dataclass(kwonly=True)
# forbid Structural pattern matching
#@dataclass(match_args=False)

# slots allows instance variable access is aboot 20% faster in slots than normal dataclass with dicts
# slots makes multiple inheritance fail because python doesn't know which functions to call 
@dataclass(slots=True)
class Person:
    name: str
    address: str
    email: str
    active: bool = True
    # if you don't define the factory, all the people will share the same values because it is a pointer to the same object
    email_addresses: list[str] = field(default_factory=list)
    # init controls if you can initialize the value or not
    id: str = field(init=False, default_factory=generate_id) 
    _search_string: str = field(init=False, default='', repr=False)
    
    def __post__init__(self) -> None:
        self._search_string = f"{self.name} {self.address} {self.email}"

    def __str__(self) -> str:
        return json.dumps(asdict(self))
    
def main() -> None:
    person = Person(name="John", address="123 Main St", email="john@doe.com")
# This throws an error when using slots because it's never created
#    print(person.__dict__["name"])
    print(person)
    
main()
