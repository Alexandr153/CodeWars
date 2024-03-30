def find_it(seq):
    counter = 0
    number = 0
    for i in seq:
        counter = seq.count(i)
        if counter % 2 == 1:
            number = i
            break
        else:
            continue

    return number



# @test.it("find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) should return 5 (because it appears 3 times)")
# def _():
#     test.assert_equals(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
#
#
# @test.it("find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) should return -1 (because it appears 1 time)")
# def _():
#     test.assert_equals(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1);
#
#
# @test.it("find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]) should return 5 (because it appears 3 times)")
# def _():
#     test.assert_equals(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5);
#
#
# @test.it("find_it([10]) should return 10 (because it appears 1 time)")
# def _():
#     test.assert_equals(find_it([10]), 10);
#
#
# @test.it("find_it([10, 10, 10]) should return 10 (because it appears 3 times)")
# def _():
#     test.assert_equals(find_it([10, 10, 10]), 10);
#
#
# @test.it("find_it([1,1,1,1,1,1,10,1,1,1,1]) should return 10 (because it appears 1 time)")
# def _():
#     test.assert_equals(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10);
#
#
# @test.it("find_it([5,4,3,2,1,5,4,3,2,10,10]) should return 1 (because it appears 1 time)")
# def _():
#     test.assert_equals(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1);