import { Inter } from "next/font/google";
import "./globals.css";

import Menu from "@/components/Menu";
import Footer from "@/components/Footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "TABA",
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-br">
      <body className={inter.className}>
        <Menu className="flex justify-end max-w-xl"/>
        {children}
        <Footer />
      </body>
    </html>
  );
}