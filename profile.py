class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")
        print(f"Fun fact about me: {self.fun_fact}")

    def show_stack(self):
        print("\nMy Tech Stack includes:")
        for tool in self.tech_stack:
            print(f" - {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}
if __name__ == "__main_":
    my_profile = Profile(
        name="Gladys Ayaa",
        favorite_language="Python",
        hobby="Reading Tech Blogs",
        tech_stack=["Python", "Django", "Git", "JavaScript", "React"],
        github_username="gladysayaa",
        fun_fact="singing along to favourite song in the car!"
    )


    my_profile.introduce()
    my_profile.show_stack()
    print("\nMy GitHub Profile:", my_profile.github_link())
