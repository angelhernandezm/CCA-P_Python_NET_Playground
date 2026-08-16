# CCA-P_Python_NET_Playground
Playground for Claude Certified Architect (Professional), Python and C# Agents

## Repository structure

```
python/     Python exercises and their pytest unit tests
csharp/     C# exercises (as .NET class libraries) and their xUnit test projects
```

Each exercise focuses on a design pattern or architecture concept relevant to
CCA-P preparation, implemented in both Python and C# where useful for
comparison.

### Python exercises

| Exercise | Description |
| --- | --- |
| [`strategy_pattern`](python/exercises/strategy_pattern) | Strategy pattern applied to a shopping cart discount calculator |

Run the Python tests:

```bash
cd python
pip install -r requirements.txt
pytest
```

### C# exercises

| Exercise | Description |
| --- | --- |
| [`Exercises.FactoryPattern`](csharp/Exercises.FactoryPattern) | Factory pattern applied to a notification sender |

Run the C# tests:

```bash
cd csharp
dotnet test
```
