# Day 11: Data Aggregation and Grouping

## groupby()

Used to divide data into groups and perform calculations.

Syntax:

```python
df.groupby("Column")
```

---

## mean()

Calculates average.

```python
df.groupby("Class").mean()
```

---

## agg()

Used to perform multiple operations together.

Example:

```python
df.groupby("Gender").agg({
    "Name":"count",
    "Math_Score":"max",
    "Science_Score":"min"
})
```

---

## Functions Used

- groupby()
- mean()
- agg()
- count
- max
- min

---

## AI/ML Connection

Grouping helps analyze datasets before model training by comparing different categories and finding useful insights.