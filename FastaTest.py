import unittest

from Classes\Fasta import Fasta


class FastaTest(unittest.TestCase):

    def test_pairs_list_return_pair(self):
        r = Fasta()
        res = r.read_fasta_file_as_list_of_pairs('Resources\BB11001.tfa')
        first = ["1aab_","GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTYIPPKGE"]
        second = ["1j46_A", "MQDRVKRPMNAFIVWSRDQRRKMALENPRMRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRPRRKAKMLPK"]
        third = ["1k99_A", "MKKLKKHPDFPKKPLTPYFRFFMEKRAKYAKLHPEMSNLDLTKILSKKYKELPEKKKMKYIQDFQREKQEFERNLARFREDHPDLIQNAKK"]
        fourth = ["2lef_A", "MHIKKPLNAFMLYMKEMRANVVAESTLKESAAINQILGRRWHALSREEQAKYYELARKERQLHMQLYPGWSARDNYGKKKKRKREK"]
        complete = [first, second, third, fourth]
        self.assertEqual(res, complete)