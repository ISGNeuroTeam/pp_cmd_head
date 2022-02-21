from pp_exec_env.base_command import BaseCommand, Syntax, Rule, pd

DEFAULT_NUMBER = 10


class HeadCommand(BaseCommand):
    syntax = Syntax([Rule(name="number", type="arg", input_types=['integer'])], use_timewindow=False)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        number = self.get_arg('number').value
        return df.head(number or DEFAULT_NUMBER)
