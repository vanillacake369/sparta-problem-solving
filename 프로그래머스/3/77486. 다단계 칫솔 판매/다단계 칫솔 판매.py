def solution(enroll, referral, seller, amount):
    finalBenefitTree = {}
    for eachEnroll in enroll:
        finalBenefitTree[eachEnroll] = 0
    parentsTree = {}
    for eachEnroll, eachReferral in zip(enroll, referral):
        parentsTree[eachEnroll] = eachReferral
    for eachSeller, eachAmount in zip(seller, amount):
        nextSeller = eachSeller
        eachAmount = eachAmount * 100
        while nextSeller in parentsTree and eachAmount > 0:
            finalBenefitTree[nextSeller] += eachAmount - eachAmount // 10
            eachAmount //= 10
            nextSeller = parentsTree[nextSeller]
    return list(finalBenefitTree.values())