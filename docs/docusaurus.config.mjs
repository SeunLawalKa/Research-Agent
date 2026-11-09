/** @type {import('@docusaurus/types').DocusaurusConfig} */
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);

export default {
  title: 'Research Agent',
  tagline: 'The leading autonomous AI research agent',
  url: 'https://docs.gptr.dev',
  baseUrl: '/',
  onBrokenLinks: 'ignore',
  //deploymentBranch: 'master',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/gptr-logo.png',
  organizationName: 'SeunLawalKa',
  trailingSlash: false,
  projectName: 'research-agent',
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],
  themeConfig: {
    navbar: {
      title: 'Research Agent',
      logo: {
        alt: 'Research Agent',
        src: 'img/gptr-logo.png',
      },
      items: [
        {
          type: 'doc',
          docId: 'welcome',
          position: 'left',
          label: 'Docs',
        },

        {to: 'blog', label: 'Blog', position: 'left'},
        {
          type: 'doc',
          docId: 'faq',
          position: 'left',
          label: 'FAQ',
        },
        {
            href: 'mailto:seunlawalka@gmail.com',
            position: 'left',
            label: 'Contact',
        },
        {
          href: 'https://github.com/SeunLawalKa/research-agent',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Community',
          items: [
            {
              label: 'Discord',
              href: 'https://discord.gg/8YkBcCED5y',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/assaf_elovic',
            },
            {
              label: 'LinkedIn',
              href: 'https://www.linkedin.com/in/assafe/',
            },
          ],
        },
        {
          title: 'Company',
          items: [
            {
              label: 'Homepage',
              href: 'https://gptr.dev',
            },
            {
              label: 'Contact',
              href: 'mailto:SeunLawalKa@gmail.com',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Research Agent.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/SeunLawalKa/research-agent/tree/master/docs',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: {
          onUntruncatedBlogPosts: 'ignore',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  stylesheets: [
    {
        href: "https://cdn.jsdelivr.net/npm/katex@0.13.11/dist/katex.min.css",
        integrity: "sha384-Um5gpz1odJg5Z4HAmzPtgZKdTBHZdw8S29IecapCSB31ligYPhHQZMIlWLYQGVoc",
        crossorigin: "anonymous",
    },
  ],

  plugins: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      {
        hashed: true,
        blogDir:"./blog/"
      },
    ],
  ],
};
