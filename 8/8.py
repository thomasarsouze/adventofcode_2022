import numpy as np

f = open("input.txt", "r")
inputs = f.read()

def parse_input(inputs):
    return np.array([[int(i) for i in l] for l in inputs.split('\n')])

# Not efficient but ok here
def visible_trees(forest):
    visible = np.full(np.shape(forest),True)
    for c in range(1,np.shape(forest)[0]):
        for l in range(1,np.shape(forest)[1]):
            tree   = forest[c,l]
            top    = forest[:c,l]
            bottom = forest[c+1:,l]
            right  = forest[c,l+1:]
            left   = forest[c,:l]
            visible[c,l] = any([all(tree > top), all(tree > bottom), all(tree > right), all(tree > left)])
    return visible

forest = parse_input(inputs)
visible = visible_trees(forest)

## Part 1
print("Nb of visible trees : ", sum(sum(visible)))

## Part 2
def scenic_score(forest):   

    def _get_score(tree, colign):
        return len(colign) if all(tree > colign) else np.nonzero(tree <= colign)[0][0]+1

    score = np.full(np.shape(forest),0)
    for c in range(1,np.shape(forest)[0]):
        for l in range(1,np.shape(forest)[1]):
            tree   = forest[l,c]
            top    = forest[:l,c]
            bottom = forest[l+1:,c]
            right  = forest[l,c+1:]
            left   = forest[l,:c]
            score_top = _get_score(tree, top[::-1])
            score_bottom = _get_score(tree, bottom)
            score_left = _get_score(tree, left[::-1])
            score_right = _get_score(tree, right)
            score[l,c] = score_top * score_bottom * score_left * score_right
    return score

score = scenic_score(forest)
print("Nb max of visible trees : ", np.max(score))