export default {
	modern: true,
	loading: {
		color: "#93C5FD",
		height: "3px",
	},
	head: {
		title: "La esquina gourmet:",
		htmlAttrs: {
			lang: "es",
		},
		meta: [
			{ charset: "utf-8" },
			{ name: "viewport", content: "width=device-width, initial-scale=1" },
			{ name: "author", content: "La esquina gourmet" },
			{ name: "description", content: "La esquina gourmet te da un mejor sabor a tu vida" },
			{ name: "format-detection", content: "telephone=no" },
			{ name: "theme-color", content: "#93C5FD" },
		],
		link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
	},

	watchers: {
		webpack: {
			poll: 5000,
		},
	},

	css: ["~/assets/sass/main.sass"],

	components: true,

	plugins: [
		{
			src: '~/plugins/axios'
		},
		{
			src: '~/plugins/axiosIntern'
		},
	],

	components: true,

	buildModules: ["@nuxtjs/tailwindcss"],

	modules: ["@nuxtjs/axios"],

	axios: {
		baseURL: "http://localhost:8000/api",
	},

	static: {
		prefix: false,
	},

	vue: {
		config: {
			productionTip: false,
			devtools: false,
			performance: true,
		},
	},

	build: {
		extractCSS: true,
		loaders: {
			limit: 800,
		},
		optimization: {
			runtimeChunk: true,
			minimize: true,
		},
		aggressiveCodeRemoval: true,
		splitChunks: {
			layouts: false,
			pages: true,
			commons: true,
		},
		followSymlinks: true,
		html: {
			minify: {
				collapseBooleanAttributes: true,
				decodeEntities: true,
				minifyCSS: true,
				minifyJS: true,
				processConditionalComments: true,
				removeEmptyAttributes: true,
				removeRedundantAttributes: true,
				trimCustomFragments: true,
				useShortDoctype: true,
				minifyURLs: true,
				removeComments: true,
				removeEmptyElements: true,
				preserveLineBreaks: false,
				collapseWhitespace: true,
			},
		},
	},

	server: {
		host: "localhost",
		port: 3000,
	},

	publicRuntimeConfig: {
		rootUrl: 'http://localhost',
		axios: {
			browserBaseURL: 'http://localhost:8000'
		}
	},

	privateRuntimeConfig: {
		axios: {
			baseURL: 'http://localhost:8000'
		}
	}
};
