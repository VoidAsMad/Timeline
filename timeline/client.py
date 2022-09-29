from typing import Dict, List


class Timeline:
    """
    연대표 작성 프로그램입니다.
    Made : VoidAsMad

    이슈와 PR은 언제든지 환영입니다!
    """

    def __init__(self) -> None:
        self.data_set: Dict = {}

    def append(self, year: str, text: str) -> None:
        """데이터를 추가합니다."""
        if self.check_overlap(year):
            texts = self.data_set[year]
            text = " ".join(texts) + f" {text}"
            self.data_set[year] = text.split(" ")
        else:
            self.data_set[year] = text

    def _return(self) -> Dict[str, List[str]]:
        """결과 데이터를 반환합니다."""
        return self.data_set

    def check_overlap(self, year) -> bool:
        """데이터의 중복여부를 체크합니다."""
        try:
            self.data_set[year]
        except:
            return False
        else:
            return True
