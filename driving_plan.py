from typing import List, Tuple

from pydantic import BaseModel

class DrivingPlan(BaseModel):
    drivings: List[Tuple[int, int]]

    def per_family(self) -> List[Tuple[int, List[int]]]:
        plan = []
        for f in sorted(list(set([f for f, w in self.drivings]))):
            plan.append([f, [w for ff, w in self.drivings if ff == f]])
        return plan

    def per_weekend(self) -> List[Tuple[int, List[int]]]:
        plan = []
        for w in sorted(list(set([w for f, w in self.drivings]))):
            plan.append([w, [f for f, ww in self.drivings if ww == w]])
        return plan

    def show(self):
        print('-'*80)
        for weekend, families in self.per_weekend():
            print(f'Weekend #{weekend}: {", ".join([f"Famille {family}" for family in families])}')
        print('-'*10)
        for family, weekends in self.per_family():
            print(f'Family #{family}: {", ".join([f"WE{weekend}" for weekend in weekends])}')
