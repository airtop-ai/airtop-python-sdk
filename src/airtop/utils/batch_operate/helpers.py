from typing import List
from .types import BatchOperationUrl

def distribute_urls_to_batches(max_concurrent_sessions: int, urls: List[BatchOperationUrl]) -> List[List[BatchOperationUrl]]:
    if len(urls) == 0:
        return []

    batch_count = min(max_concurrent_sessions, len(urls))
    batches: List[List[BatchOperationUrl]] = [[] for _ in range(batch_count)]
    for i, url in enumerate(urls):
        batches[i % batch_count].append(url)
    return batches