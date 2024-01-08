# BigONavigator - Navigating Computational Complexity

**BigONavigator** is not just a Python package; it's a journey into the heart of algorithm efficiency. Originally developed as a university project, this tool has grown into a robust resource for developers, researchers, and students alike. It elegantly navigates the complexities of computational performance, providing insights into the Big O notation of algorithms with precision and clarity.

### 🎓 University Project Background
This project was conceived and developed as part of a university course in Computer Science, aiming to bridge theoretical concepts with practical application. It offers an educational insight into algorithm complexity, making it a perfect tool for academic projects and research.

### 🌟 Key Features
- **Dynamic Complexity Estimation**: Intuitively estimate the computational complexity of Python functions. (COMING SOON)
- **Decorator-Driven Analysis**: Utilize decorators to effortlessly mark and track function complexities.
- **Comprehensive Complexity Table**: View a summarised table of all tracked functions and their complexities, fostering a deeper understanding of algorithm performance.

## 🛠 Installation

```bash
pip install BigONavigator
```

## 📈 Usage

Kickstart your complexity analysis with BigONavigator:

```python
from bigonavigator import O
from bigonavigator import show_complexity_table

@O['n']
def example_linear_function(data):
    # Implement linear time complexity operations
    pass

# Review the complexity summary
show_complexity_table()
```

## 📚 Documentation

Delve deeper into BigONavigator with our comprehensive documentation, which covers everything from setup to advanced features. Perfect for academic purposes and hands-on learning. Check it out [here](./DOCS.md).

## 🤝 Contributing

Your contributions can help make BigONavigator an even more valuable tool for the academic and developer community:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourAmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/YourAmazingFeature`)
5. Open a Pull Request

## 📞 Support & Feedback

We welcome feedback and queries! Please file any issues or suggestions on our [Issues page](https://github.com/velocitatem/BigONavigator/issues) or engage with us via [Discussions](https://github.com/velocitatem/BigONavigator/discussions).

## 📃 License

This project is open-source and available under the MIT License. See `LICENSE` for more details.
