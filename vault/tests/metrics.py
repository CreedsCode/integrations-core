# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# Everything our environment may provides
METRICS = {
    'go.gc.duration.seconds',
    'go.goroutines',
    'go.info',
    'go.memstats.alloc.bytes',
    'go.memstats.alloc.bytes.total',
    'go.memstats.buck_hash.sys.bytes',
    'go.memstats.frees.total',
    'go.memstats.gc.cpu.fraction',
    'go.memstats.gc.sys.bytes',
    'go.memstats.heap.alloc.bytes',
    'go.memstats.heap.idle.bytes',
    'go.memstats.heap.inuse.bytes',
    'go.memstats.heap.objects',
    'go.memstats.heap.released.bytes',
    'go.memstats.heap.sys.bytes',
    'go.memstats.last.gc.time.seconds',
    'go.memstats.lookups.total',
    'go.memstats.mallocs.total',
    'go.memstats.mcache.inuse.bytes',
    'go.memstats.mcache.sys.bytes',
    'go.memstats.mspan.inuse.bytes',
    'go.memstats.mspan.sys.bytes',
    'go.memstats.next.gc.bytes',
    'go.memstats.other.sys.bytes',
    'go.memstats.stack.inuse.bytes',
    'go.memstats.stack.sys.bytes',
    'go.memstats.sys.bytes',
    'go.threads',
    'process.cpu.seconds.total',
    'process.max.fds',
    'process.open.fds',
    'process.resident_memory.bytes',
    'process.start_time.seconds',
    'process.virtual_memory.bytes',
    'process.virtual_memory.max.bytes',
    'vault.audit.log.request',
    'vault.audit.log.request.failure',
    'vault.barrier.get',
    'vault.barrier.put',
    'vault.consul.put',
    'vault.core.check.token',
    'vault.core.fetch.acl_and_token',
    'vault.expire.fetch.lease.times',
    'vault.expire.fetch.lease.times.by_token',
    'vault.expire.num_leases',
    'vault.policy.get_policy',
    'vault.rollback.attempt.auth.jwt',
    'vault.rollback.attempt.auth.token',
    'vault.rollback.attempt.cubbyhole',
    'vault.rollback.attempt.identity',
    'vault.rollback.attempt.sys',
    'vault.route.rollback.auth.jwt',
    'vault.route.rollback.auth.token',
    'vault.route.rollback.cubbyhole',
    'vault.route.rollback.identity',
    'vault.route.rollback.sys',
    'vault.runtime.alloc.bytes',
    'vault.runtime.free.count',
    'vault.runtime.heap.objects',
    'vault.runtime.malloc.count',
    'vault.runtime.num_goroutines',
    'vault.runtime.sys.bytes',
    'vault.runtime.gc.pause_ns',
    'vault.runtime.total.gc.pause_ns',
    'vault.runtime.total.gc.runs',
    'vault.token.lookup',
}
