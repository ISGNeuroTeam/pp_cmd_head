import pandas as pd
from otlang.sdk.syntax import Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax

DEFAULT_NUMBER = 10


class HeadCommand(BaseCommand):
    syntax = Syntax([Positional("number", otl_type=OTLType.INTEGER)], use_timewindow=False)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        number = self.get_arg('number').value
        return df.head(number or DEFAULT_NUMBER)
