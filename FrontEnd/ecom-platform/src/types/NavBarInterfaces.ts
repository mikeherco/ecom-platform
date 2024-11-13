export interface NavBarItem {
  id: number;
  meta: {
    type: string;
    detail_url: string;
    slug: string;
    first_published_at: string;
  };
  title: string;
}

export interface NavBarDetail {
  id: number;
  meta: {
    type: string;
    detail_url: string;
    html_url: string | null;
    slug: string;
    show_in_menus: boolean;
    seo_title: string;
    search_description: string;
    first_published_at: string;
    alias_of: string | null;
    parent: {
      id: number;
      meta: {
        type: string;
        detail_url: string;
        html_url: string | null;
      };
      title: string;
    };
  };
  title: string;
  desc: Array<{
    type: string;
    value: number;
    id: string;
  }>;
  navbar_categorias: Array<{
    id: number;
    meta: {
      type: string;
    };
    mostrar: boolean;
    nombre: string;
  }>;
}

export interface Categoria {
  id: number;
  meta: {
    type: string;
  };
  mostrar: boolean;
  nombre: string;
}
