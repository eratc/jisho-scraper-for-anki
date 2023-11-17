from dataclasses import dataclass


@dataclass
class Verb:
    word: str
    pos: str
    caption: str


class V1(Verb):
    def base(self):
        return self.word

    def renyokei(self):
        return self.word.removesuffix('る')

    mizenkei = meireikei = takei = renyokei

    def non_past_p(self):
        return self.base()

    def non_past_n(self):
        return f"{self.mizenkei()}ない"

    def masu_p(self):
        return f"{self.renyokei()}ます"

    def masu_n(self):
        return f"{self.renyokei()}ません"

    def past_p(self):
        return f"{self.takei()}た"

    def past_n(self):
        return f"{self.mizenkei()}なかった"

    def past_polite_p(self):
        return f"{self.renyokei()}ました"

    def past_polite_n(self):
        return f"{self.renyokei()}ませんでした"

    def te_p(self):
        return f"{self.takei()}て"

    def te_n(self):
        return f"{self.mizenkei()}なくて"

    def potential_p(self):
        return f"{self.mizenkei()}られる"

    def potential_n(self):
        return f"{self.mizenkei()}られない"

    def passive_p(self):
        return f"{self.mizenkei()}られる"

    def passive_n(self):
        return f"{self.mizenkei()}られない"

    def causative_p(self):
        return f"{self.mizenkei()}させる"

    def causative_n(self):
        return f"{self.mizenkei()}させない"

    def causative_passive_p(self):
        return f"{self.mizenkei()}させられる"

    def causative_passive_n(self):
        return f"{self.mizenkei()}させられない"

    def imperative_p(self):
        return f"{self.meireikei()}ろ"

    def imperative_n(self):
        return f"{self.base()}な"


class Godan(Verb):
    def base(self):
        return self.word

    def renyokei(self):
        return f'{self.word[:-1]}{self.v5_patterns[self.pos][0]}'

    def mizenkei(self):
        return f'{self.word[:-1]}{self.v5_patterns[self.pos][1]}'

    def meireikei(self):
        return f'{self.word[:-1]}{self.v5_patterns[self.pos][2]}'

    def takei(self):
        return f'{self.word[:-1]}{self.v5_patterns[self.pos][3]}'

    v5_patterns = {
        'v5u': ['い', 'わ', 'え', 'っ'],
        'v5k': ['き', 'か', 'け', 'い'],
        'v5k-s': ['き', 'か', 'け', 'っ'],
        'v5g': ['ぎ', 'が', 'げ', 'い'],
        'v5m': ['み', 'ま', 'め', 'ん'],
        'v5n': ['に', 'な', 'ね', 'ん'],
        'v5r': ['り', 'ら', 'れ', 'っ'],
        'v5b': ['び', 'ば', 'べ', 'ん'],
        'v5s': ['し', 'さ', 'せ', 'し'],
        'v5t': ['ち', 'た', 'て', 'っ'],
        'v5z': ['じ', 'ざ', 'ぜ', 'い']
    }

    def non_past_p(self):
        return self.base()

    def non_past_n(self):
        return f"{self.mizenkei()}ない"

    def masu_p(self):
        return f"{self.renyokei()}ます"

    def masu_n(self):
        return f"{self.renyokei()}ません"

    def past_p(self):
        if self.pos == 'v5g' or self.pos == 'v5m' or self.pos == 'v5n' or self.pos == 'v5b':
            return f"{self.takei()}だ"
        else:
            return f"{self.takei()}た"

    def past_n(self):
        return f"{self.mizenkei()}なかった"

    def past_polite_p(self):
        return f"{self.renyokei()}ました"

    def past_polite_n(self):
        return f"{self.renyokei()}ませんでした"

    def te_p(self):
        if self.pos == 'v5g' or self.pos == 'v5m' or self.pos == 'v5n' or self.pos == 'v5b':
            return f"{self.takei()}で"
        else:
            return f"{self.takei()}て"

    def te_n(self):
        return f"{self.mizenkei()}なくて"

    def potential_p(self):
        return f"{self.meireikei()}る"

    def potential_n(self):
        return f"{self.meireikei()}ない"

    def passive_p(self):
        return f"{self.mizenkei()}れる"

    def passive_n(self):
        return f"{self.mizenkei()}れない"

    def causative_p(self):
        return f"{self.mizenkei()}せる"

    def causative_n(self):
        return f"{self.mizenkei()}せない"

    def causative_passive_p(self):
        return f"{self.mizenkei()}せられる"

    def causative_passive_n(self):
        return f"{self.mizenkei()}せられない"

    def imperative_p(self):
        return f"{self.meireikei()}"

    def imperative_n(self):
        return f"{self.base()}な"


class Kuru(Verb):
    def base(self):
        return self.word

    def renyokei(self):
        return self.word.removesuffix('る')

    mizenkei = meireikei = takei = renyokei

    # ku
    def non_past_p(self):
        return self.base()

    # ko
    def non_past_n(self):
        return f"{self.mizenkei()}ない"

    # ki
    def masu_p(self):
        return f"{self.renyokei()}ます"

    # ki
    def masu_n(self):
        return f"{self.renyokei()}ません"

    # ki
    def past_p(self):
        return f"{self.takei()}た"

    # ko
    def past_n(self):
        return f"{self.mizenkei()}なかった"

    # ki
    def past_polite_p(self):
        return f"{self.renyokei()}ました"

    # ki
    def past_polite_n(self):
        return f"{self.renyokei()}ませんでした"

    # ki
    def te_p(self):
        return f"{self.takei()}て"

    # ko
    def te_n(self):
        return f"{self.mizenkei()}なくて"

    # ko
    def potential_p(self):
        return f"{self.mizenkei()}られる"

    # ko
    def potential_n(self):
        return f"{self.mizenkei()}られない"

    # ko
    def passive_p(self):
        return f"{self.mizenkei()}られる"

    # ko
    def passive_n(self):
        return f"{self.mizenkei()}られない"

    # ko
    def causative_p(self):
        return f"{self.mizenkei()}させる"

    # ko
    def causative_n(self):
        return f"{self.mizenkei()}させない"

    # ko
    def causative_passive_p(self):
        return f"{self.mizenkei()}させられる"

    # ko
    def causative_passive_n(self):
        return f"{self.mizenkei()}させられない"

    # ko
    def imperative_p(self):
        return f"{self.meireikei()}い"

    # ku
    def imperative_n(self):
        return f"{self.base()}な"


class SuruOnly(Verb):
    def base(self):
        return self.word.removesuffix('る')

    def renyokei(self):
        return 'し'

    mizenkei = meireikei = takei = renyokei

    # su
    def non_past_p(self):
        return f"{self.base()}る"

    # shi
    def non_past_n(self):
        return f"{self.base()}ない"

    # shi
    def masu_p(self):
        return f"{self.base()}ます"

    # shi
    def masu_n(self):
        return f"{self.base()}ません"

    # shi
    def past_p(self):
        return f"{self.base()}た"

    # shi
    def past_n(self):
        return f"{self.base()}なかった"

    # shi
    def past_polite_p(self):
        return f"{self.base()}ました"

    # shi
    def past_polite_n(self):
        return f"{self.base()}ませんでした"

    # shi
    def te_p(self):
        return f"{self.base()}て"

    # shi
    def te_n(self):
        return f"{self.base()}なくて"

    def potential_p(self):
        return "できる"

    def potential_n(self):
        return "できない"

    # sa
    def passive_p(self):
        return f"{self.base()}れる"

    # sa
    def passive_n(self):
        return f"{self.base()}れない"

    # sa
    def causative_p(self):
        return f"{self.base()}せる"

    # sa
    def causative_n(self):
        return f"{self.base()}せない"

    # sa
    def causative_passive_p(self):
        return f"{self.base()}せられる"

    # sa
    def causative_passive_n(self):
        return f"{self.base()}せられない"

    # shi
    def imperative_p(self):
        return f"{self.base()}ろ"

    # su
    def imperative_n(self):
        return f"{self.base()}るな"


class SuruDerivative(Verb):
    def base(self):
        return self.word.removesuffix("する")

    def renyokei(self):
        return 'し'

    mizenkei = meireikei = takei = renyokei

    def non_past_p(self):
        return f"{self.base()}する"

    def non_past_n(self):
        return f"{self.base()}しない"

    def masu_p(self):
        return f"{self.base()}します"

    def masu_n(self):
        return f"{self.base()}しません"

    def past_p(self):
        return f"{self.base()}した"

    def past_n(self):
        return f"{self.base()}しなかった"

    def past_polite_p(self):
        return f"{self.base()}しました"

    def past_polite_n(self):
        return f"{self.base()}しませんでした"

    def te_p(self):
        return f"{self.base()}して"

    def te_n(self):
        return f"{self.base()}しなくて"

    def potential_p(self):
        return f"{self.base()}できる"

    def potential_n(self):
        return f"{self.base()}できない"

    def passive_p(self):
        return f"{self.base()}られる"

    def passive_n(self):
        return f"{self.base()}られない"

    def causative_p(self):
        return f"{self.base()}させる"

    def causative_n(self):
        return f"{self.base()}させない"

    def causative_passive_p(self):
        return f"{self.base()}させられる"

    def causative_passive_n(self):
        return f"{self.base()}させられない"

    def imperative_p(self):
        return f"{self.base()}しろ"

    def imperative_n(self):
        return f"{self.base()}するな"
