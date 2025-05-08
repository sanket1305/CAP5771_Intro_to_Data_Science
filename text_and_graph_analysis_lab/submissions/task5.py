# FREEZE CODE BEGIN
import numpy as np

def compute_pagerank(pages: dict[str, list[str]], damping: float = 0.85, max_iter: int = 100, tol: float = 1e-6) -> dict[str, float]:
    nodes = list(pages.keys())
    N = len(nodes)
    node_index = {node: i for i, node in enumerate(nodes)}

    pr = np.full(N, 1.0 / N)  # Initial PageRank scores
    M = np.zeros((N, N))      # Link-based transition matrix

    for page, links in pages.items():
        if links:
            weight = 1 / len(links)
            for dest in links:
                if dest in node_index:
                    M[node_index[dest], node_index[page]] += weight
        else:
            M[:, node_index[page]] += 1.0 / N  # Spread evenly for dangling nodes

    for _ in range(max_iter):
        # Step 2: Assign some probability to randomly jumping to any page
        base = None  # Hint: Depends on total number of pages and damping factor
        # FREEZE CODE END
# WRITE YOUR CODE HERE
        # FREEZE CODE BEGIN

        # Step 3: Calculate how much rank each page receives from its incoming links
        contrib = None  # Hint: Combine the link matrix M with the current ranks
        # FREEZE CODE END
# WRITE YOUR CODE HERE
        # FREEZE CODE BEGIN

        # Step 4: Update ranks by combining random jumps with link-based scores
        new_pr = None  # Hint: Blend the base and contribution with the damping factor
        # FREEZE CODE END
# WRITE YOUR CODE HERE
        # FREEZE CODE BEGIN

        # Step 5: Stop if the scores have stabilized
        if np.linalg.norm(new_pr - pr, 1) < tol:
            break
        pr = new_pr

    return {node: round(score, 6) for node, score in zip(nodes, pr)}
# FREEZE CODE END

compute_pagerank