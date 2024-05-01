from shadycompass import ConfigFact
from shadycompass.config import SECTION_TOOLS, ToolCategory, ToolRecommended
from shadycompass.rules.http_buster.gobuster import GoBusterRules
from tests.tests import assertFactIn
from tests.rules.base import RulesBase


class GobusterTest(RulesBase):

    def __init__(self, methodName: str = ...):
        super().__init__(None, methodName)

    def test_gobuster(self):
        self.engine.declare(
            ConfigFact(section=SECTION_TOOLS, option=ToolCategory.http_buster, value=GoBusterRules.gobuster_tool_name, global0=True))
        self.engine.run()
        assertFactIn(ToolRecommended(
            category=ToolCategory.http_buster,
            name=GoBusterRules.gobuster_tool_name,
            command_line=[
                'dir', '--random-agent', '--discover-backup', '-k',
                '-o', "gobuster-8080-hospital.htb.txt",
                '-u', 'http://hospital.htb:8080'
            ],
        ), self.engine)
        assertFactIn(ToolRecommended(
            category=ToolCategory.http_buster,
            name=GoBusterRules.gobuster_tool_name,
            command_line=[
                'dir', '--random-agent', '--discover-backup', '-k',
                '-o', "gobuster-443-hospital.htb.txt",
                '-u', 'https://hospital.htb:443'
            ],
        ), self.engine)