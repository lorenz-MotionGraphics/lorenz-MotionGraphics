[![lorenz miguel gracia](https://img.shields.io/badge/lorenz%20miguel%20gracia-enthusiast%20in%20web%20developments-green?labelColor=lightblue&style=flat-square&link=https://l.facebook.com/l.php?u=http%3A%2F%2Flucidtechinnovations.rf.gd%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAAR1g5k-2MO8dEvGVRDLpA5cpVzHRVlUGDd-8q2hrFs8OInsZrPhAOb2jwo0_aem_AbLdEjIzr8haC2Nsm5lSG5RbKLwYiM0ysXKWCi1-jpmiF0NyaIz4WxauwktN4qI7_cmz_UhB0C6NXzQbHNkCNOsO&h=AT31zfVo1XRF4-SVz0JyTAP17WpmOThVcUn0130zhNKBFxWv4-HRmZupCQ1z_JYakd9SOrZ9uKxe6LBKyQVxwIUaeogLFhe37KBP4-5uPYuxjI1TO5IZlUeO663rLUr1MoWaNA)](https://l.facebook.com/l.php?u=http%3A%2F%2Flucidtechinnovations.rf.gd%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAAR1g5k-2MO8dEvGVRDLpA5cpVzHRVlUGDd-8q2hrFs8OInsZrPhAOb2jwo0_aem_AbLdEjIzr8haC2Nsm5lSG5RbKLwYiM0ysXKWCi1-jpmiF0NyaIz4WxauwktN4qI7_cmz_UhB0C6NXzQbHNkCNOsO&h=AT31zfVo1XRF4-SVz0JyTAP17WpmOThVcUn0130zhNKBFxWv4-HRmZupCQ1z_JYakd9SOrZ9uKxe6LBKyQVxwIUaeogLFhe37KBP4-5uPYuxjI1TO5IZlUeO663rLUr1MoWaNA)

![](src/image/LORENZ%20MIGUEL%20GRACIA.png?raw=true)

### 4. Sequence Diagram using Mermaid

If you want to represent interactions between different entities, a sequence diagram can be useful.

```markdown
```mermaid
sequenceDiagram
    participant A as Start
    participant B as Condition
    participant C as Action 1
    participant D as Action 2
    participant E as End

    A->>B: Check condition
    alt Condition is true
        B->>C: Perform Action 1
    else Condition is false
        B->>D: Perform Action 2
    end
    C->>E: End
    D->>E: End
