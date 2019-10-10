## Data faker

### What does it do?

TS Faker provides a method to generate fake data for products and manufacturers to benchmark API and Import performance.

### How is it used?

#### 1. Generate sample data

Use `init.py [products] [categories] [manufacturers]`

```bash
$ python init.py 5000 0 10
```

#### 2. Run import to test Performance

Currenty there are two implementations (using redis `set` and `mset` )

````bash
$ python import.py product-5000.json
$ python import_mset.py product-5000.json
````
