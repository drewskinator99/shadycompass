from base import RulesBase
from shadycompass import ConfigFact
from shadycompass.config import SECTION_TOOLS, ToolCategory, ToolRecommended
from tests.tests import assertFactIn


class GobusterTest(RulesBase):

    def __init__(self, methodName: str = ...):
        super().__init__(None, methodName)

    def test_gobuster(self):
        self.engine.declare(
            ConfigFact(section=SECTION_TOOLS, option=ToolCategory.http_buster, value='gobuster', global0=True))
        self.engine.run()
        assertFactIn(ToolRecommended(
            category=ToolCategory.http_buster,
            name='gobuster',
            command_line=['http://hospital.htb:5985'],
        ), self.engine)
        assertFactIn(ToolRecommended(
            category=ToolCategory.http_buster,
            name='gobuster',
            command_line=['http://hospital.htb:8080'],
        ), self.engine)
        assertFactIn(ToolRecommended(
            category=ToolCategory.http_buster,
            name='gobuster',
            command_line=['https://hospital.htb:443'],
        ), self.engine)