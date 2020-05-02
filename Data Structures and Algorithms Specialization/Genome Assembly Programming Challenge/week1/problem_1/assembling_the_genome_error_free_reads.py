# python3
import sys


class SuffixArray:
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """

    def __init__(self, text):
        self.order = self.build_suffix_array(text)

    def _input(self):
        self.text = sys.stdin.readline().strip()

    @staticmethod
    def sort_characters(s):
        len_s = len(s)
        order = [0] * len_s
        count = dict()
        for i in range(len_s):
            count[s[i]] = count.get(s[i], 0) + 1
        char_list = sorted(count.keys())
        prev_char = char_list[0]
        for char in char_list[1:]:
            count[char] += count[prev_char]
            prev_char = char
        for i in range(len_s - 1, -1, -1):
            c = s[i]
            count[c] = count[c] - 1
            order[count[c]] = i
        return order

    @staticmethod
    def compute_char_classes(s, order):
        len_s = len(s)
        char_class = [0] * len_s
        char_class[order[0]] = 0
        for i in range(1, len_s):
            if s[order[i]] != s[order[i - 1]]:
                char_class[order[i]] = char_class[order[i - 1]] + 1
            else:
                char_class[order[i]] = char_class[order[i - 1]]
        return char_class

    @staticmethod
    def sort_doubled(s, length, order, _class):
        s_len = len(s)
        count = [0] * s_len
        new_order = [0] * s_len
        for i in range(s_len):
            count[_class[i]] += 1
        for j in range(1, s_len):
            count[j] += count[j - 1]
        for i in range(s_len - 1, -1, -1):
            start = (order[i] - length + s_len) % s_len
            cl = _class[start]
            count[cl] -= 1
            new_order[count[cl]] = start
        return new_order

    @staticmethod
    def update_classes(new_order, _class, length):
        n = len(new_order)
        new_class = [0] * n
        new_class[new_order[0]] = 0
        for i in range(1, n):
            curr = new_order[i]
            prev = new_order[i - 1]
            mid = curr + length
            mid_prev = (prev + length) % n
            if _class[curr] != _class[prev] or _class[mid] != _class[mid_prev]:
                new_class[curr] = new_class[prev] + 1
            else:
                new_class[curr] = new_class[prev]
        return new_class

    def build_suffix_array(self, s):
        s_len = len(s)
        order = self.sort_characters(s)
        _class = self.compute_char_classes(s, order)
        length = 1
        while length < s_len:
            order = self.sort_doubled(s, length, order, _class)
            _class = self.update_classes(order, _class, length)
            length = 2 * length
        return order


class Assembling1:
    # Genome assembly from error-free reads
    def __init__(self):
        reads = self.read_data()
        genome = self.assembly(reads)
        print(genome)

    @staticmethod
    def read_data():
        return list(set(sys.stdin.read().strip().split()))

    @staticmethod
    def bwt_from_suffix_array(text, order):
        len_t = len(text)
        bwt = [''] * len_t
        for i in range(len_t):
            bwt[i] = text[(order[i] + len_t - 1) % len_t]

        counts = dict()
        starts = dict()
        for char in alphabet:
            counts[char] = [0] * (len_t + 1)
        for i in range(len_t):
            curr_char = bwt[i]
            for char, count in counts.items():
                counts[char][i + 1] = counts[char][i]
            counts[curr_char][i + 1] += 1
        curr_index = 0
        for char in sorted(alphabet):
            starts[char] = curr_index
            curr_index += counts[char][len_t]
        return bwt, starts, counts

    def find_longest_overlap(self, text, patterns, k=12):
        order = SuffixArray(text).order
        bwt, starts, counts = self.bwt_from_suffix_array(text, order)
        len_t = len(text) - 1

        occs = dict()
        for i, p in enumerate(patterns):
            pattern = p[:k]
            top = 0
            bottom = len(bwt) - 1
            curr_index = len(pattern) - 1
            while top <= bottom:
                if curr_index >= 0:
                    symbol = pattern[curr_index]
                    curr_index -= 1
                    if counts[symbol][bottom + 1] - counts[symbol][top] > 0:
                        top = starts[symbol] + counts[symbol][top]
                        bottom = starts[symbol] + counts[symbol][bottom + 1] - 1
                    else:
                        break
                else:
                    for j in range(top, bottom + 1):
                        if not order[j] in occs:
                            occs[order[j]] = []
                        occs[order[j]].append(i)
                    break
        overlap = 0
        for pos, iList in sorted(occs.items()):
            for i in iList:
                if text[pos:-1] == patterns[i][:len_t - pos]:
                    return i, len_t - pos
        return None, overlap

    def assembly(self, reads):
        genome = reads[0]
        curr_ind = 0
        first_read = reads[curr_ind]
        while True:
            curr_read = reads[curr_ind]
            if 1 == len(reads):
                break
            del reads[curr_ind]
            curr_ind, overlap = self.find_longest_overlap(curr_read + '$', reads)
            genome += reads[curr_ind][overlap:]
        curr_ind, overlap = self.find_longest_overlap(reads[0] + '$', [first_read])
        if overlap > 0:
            return genome[:-overlap]
        else:
            return genome


if __name__ == '__main__':
    alphabet = ['$', 'A', 'C', 'G', 'T']
    Assembling1()
