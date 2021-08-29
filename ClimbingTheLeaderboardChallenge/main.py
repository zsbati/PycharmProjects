def climbingLeaderboard(ranked, player):
    # Write your code here

    out = []  # output positions here
    rank_set = set(ranked)
    ranks = list(rank_set)
    ranks.sort(reverse=True)

    for i in range(len(player)):
        score = player[i]

        if score >= ranks[0]:
            out.append(1)
            if score > ranks[0]:
                ranks.insert(0, score)

        elif score <= ranks[len(ranks) - 1]:
            if score == ranks[len(ranks)-1]:
                out.append(len(ranks))
            if score != ranks[len(ranks)-1]:
                out.append(len(ranks)+1)
                ranks.append(score)

        else:
            for j in range(len(ranks)-1):
                if score == ranks[j]:
                    out.append(j+1)
                    break
                if (score-ranks[j])*(score-ranks[j+1]) < 0:
                    out.append(j+2)
                    break

    return out


ranked = [100, 90, 90, 80]
player = [70, 80, 105]
print(climbingLeaderboard(ranked, player))
