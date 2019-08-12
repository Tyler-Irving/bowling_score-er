bowlers_score: list = []
final_score: list = []


def alpha_scorer(frames):
    scores = []
    for i in range(len(frames)):
        frame = frames[i]
        score = sum(frame)
        if score == 10:
            next_frame = frames[i + 1]
            score += next_frame[0]
        scores.append(score)
    return sum(scores)


for i in range(10):
    throw1 = int(input("First throw: "))
    if throw1 == 10:
        strike_frame: list = [throw1]
        final_score.append(sum(strike_frame))
        bowlers_score.append(strike_frame)
    elif throw1 < 10:
        throw2 = int(input("Second throw: "))
        spare_frame: list = [throw1, throw2]
        final_score.append(sum(spare_frame))
        bowlers_score.append(spare_frame)
    if len(bowlers_score) == 10:
        print(bowlers_score)
        if sum(bowlers_score[-1]) == 10:
            last_two_frames = 0
            while last_two_frames != 2:
                throw3 = int(input("Extra frame throw: "))
                if throw3 == 10:
                    final_strike_frame: list = [throw3]
                    final_score.append(sum(final_strike_frame))
                    bowlers_score.append(final_strike_frame)
                    last_two_frames += 1
                elif throw3 < 10:
                    thorw4 = int(input("Second extra frame throw: "))
                    final_spare_frame: list = [throw1, thorw4]
                    final_score.append(sum(final_spare_frame))
                    bowlers_score.append(final_spare_frame)
                    last_two_frames += 1
                if len(bowlers_score) == 12:
                    print(alpha_scorer(bowlers_score))
                    break
        else:
            print(alpha_scorer(bowlers_score))
            break
    print(bowlers_score)
