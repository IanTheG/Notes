import './style.scss'

const skills = [
  {
    name: 'React',
    value: 3,
  },
  {
    name: 'Angular',
    value: 1,
  },
  {
    name: 'Vue',
    value: 3,
  },
  {
    name: 'Vuetify',
    value: 3,
  },
  {
    name: 'TypeScript',
    value: 3,
  },
  {
    name: 'AWS',
    value: 2,
  },
  {
    name: 'MongoDB',
    value: 3,
  },
  {
    name: 'Redux',
    value: 2,
  },
  {
    name: 'GraphQL',
    value: 1,
  },
  {
    name: 'HTML5',
    value: 3,
  },
  {
    name: 'CSS, SCSS',
    value: 2,
  },
  {
    name: 'Python',
    value: 1,
  },
  {
    name: 'Java',
    value: 2,
  },
  {
    name: 'SpringBoot',
    value: 2,
  },
  {
    name: 'Groovy',
    value: 1
  },
  {
    name: 'Git, GitHub',
    value: 2,
  },
  {
    name: 'NodeJS',
    value: 2,
  },
  {
    name: 'Express',
    value: 3
  },
  {
    name: 'SQL',
    value: 2,
  },
  {
    name: 'REST APIs',
    value: 3,
  },
  // {
  //   name: 'Max MSP',
  //   value: 2,
  // },
];

skills.sort((a, b) => {
  let skillA = a.name.toUpperCase();
  let skillB = b.name.toUpperCase();
  return skillA < skillB ? -1 : skillA > skillB ? 1 : 0;
});

const rating = (value) => {
  switch (value) {
    case 1: {
      return `
        <div class="circle circle--filled"></div>
        <div class="circle"></div>
        <div class="circle"></div>
      `
    }
    case 2: {
      return `
        <div class="circle circle--filled"></div>
        <div class="circle circle--filled"></div>
        <div class="circle"></div>
      `
    }
    case 3: {
      return `
        <div class="circle circle--filled"></div>
        <div class="circle circle--filled"></div>
        <div class="circle circle--filled"></div>
      `
    }
  }
}

let skillsHTML = ''.concat(...skills.map((skill) => `
  <div class="skill-box">
  <h3>${skill.name}</h3>
  <div class="circle-box">
    ${rating(skill.value)}
  </div>
  </div>
`
));

document.getElementById('skills-box').innerHTML = skillsHTML;
